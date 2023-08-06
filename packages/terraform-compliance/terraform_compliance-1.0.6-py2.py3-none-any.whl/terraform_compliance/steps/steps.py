# -*- coding: utf-8 -*-

from radish import world, given, when, then, step
from terraform_compliance.steps import encryption_property
from terraform_compliance.common.helper import check_sg_rules, convert_resource_type, find_root_by_key, seek_key_in_dict
from terraform_compliance.common.helper import seek_regex_key_in_dict_values, jsonify
from terraform_compliance.extensions.ext_radish_bdd import skip_step
from terraform_compliance.extensions.ext_radish_bdd import custom_type_any, custom_type_condition, custom_type_section
import re
from terraform_compliance.common.exceptions import Failure, TerraformComplianceNotImplemented


# TODO: Figure out how the IAM policies/statements shown in the plan.out
# TODO: Implement an IAM Compliance via https://github.com/Netflix-Skunkworks/policyuniverse


@given(u'I have {name:ANY} defined')
@given(u'I have {name:ANY} {type_name:SECTION} configured')
def i_have_name_section_configured(_step_obj, name, type_name='resource', _terraform_config=world):
    '''
    Finds given resource or variable by name and returns it. Skips the step (and further steps) if it is not found.

    :param _step_obj: Internal, step object for radish.
    :param name: String of the name of the resource_type or variable.
    :param type_name: String of the type, either resource(s) or variable(s)
    :param _terraform_config: Internal, terraform configuration.
    :return:
    '''
    assert (type_name in ['resource', 'resources',
                          'variable', 'variables',
                          'provider', 'providers']), \
        '{} configuration type does not exist or not implemented yet. ' \
        'Use resource(s), provider(s) or variable(s) instead.'.format(type_name)

    if type_name.endswith('s'):
        type_name = type_name[:-1]

    if name == 'resource that supports tags':
        resource_types_supports_tags = find_root_by_key(_terraform_config.config.terraform.resources,
                                                        'tags',
                                                        return_key='type')
        resource_list = []
        for resource_type in resource_types_supports_tags:
            resource_list.extend(_terraform_config.config.terraform.find_resources_by_type(resource_type))

        if resource_list:
            _step_obj.context.type = type_name
            _step_obj.context.name = name
            _step_obj.context.stash = resource_list
            return True

    elif type_name == 'resource':
        name = convert_resource_type(name)
        resource_list = _terraform_config.config.terraform.find_resources_by_type(name)

        if resource_list:
            _step_obj.context.type = type_name
            _step_obj.context.name = name
            _step_obj.context.stash = resource_list
            return True

    elif type_name == 'variable':
        found_variable = _terraform_config.config.terraform.variables.get(name, None)

        if found_variable:
            _step_obj.context.type = type_name
            _step_obj.context.name = name
            _step_obj.context.stash = found_variable
            return True

    elif type_name == 'provider':
        found_provider = _terraform_config.config.terraform.configuration.get('providers', {}).get(name, None)

        if found_provider:
            _step_obj.context.type = type_name
            _step_obj.context.name = name
            _step_obj.context.stash = found_provider
            return True

    skip_step(_step_obj, name)


@when(u'it contain {something:ANY}')
@when(u'they have {something:ANY}')
@when(u'it has {something:ANY}')
@when(u'it contains {something:ANY}')
@then(u'it must contain {something:ANY}')
def it_condition_contain_something(_step_obj, something):
    prop_list = []

    if _step_obj.context.type == 'resource':
        for resource in _step_obj.context.stash:
            if type(resource) is not dict:
                resource = {'values': resource,
                            'address': resource,
                            'type': _step_obj.context.name}

            values = resource.get('values', {})

            found_value = None
            found_key = None
            if type(values) is dict:
                found_key = seek_key_in_dict(values, something)
                if len(found_key):
                    found_key = found_key[0]

                    if type(found_key) is dict:
                        found_value = jsonify(found_key[something])

            if found_key:
                prop_list.append({'address': resource['address'],
                                  'values': found_value,
                                  'type': _step_obj.context.name})

            elif 'must' in _step_obj.context_sensitive_sentence:
                raise Failure('{} ({}) does not have {} property.'.format(resource['address'],
                                                                          resource.get('type', ''),
                                                                          something))

        if prop_list:
            _step_obj.context.stash = prop_list
            _step_obj.context.property_name = something
            return True

        skip_step(_step_obj,
                  resource=_step_obj.context.name,
                  message='Can not find any {} property for {} resource in '
                          'terraform plan.'.format(something, _step_obj.context.name))

    elif _step_obj.context.type == 'provider':
        values = seek_key_in_dict(_step_obj.context.stash, something)

        if values:
            _step_obj.context.stash = values
            _step_obj.context.property_name = something
            return True

    skip_step(_step_obj,
              resource=_step_obj.context.name,
              message='Skipping the step since {} type does not have {} property.'.format(_step_obj.context.type,
                                                                                          something))


@then(u'encryption is enabled')
@then(u'encryption must be enabled')
def encryption_is_enabled(_step_obj):
    for resource in _step_obj.context.stash:
        if type(resource) is dict:
            prop = encryption_property.get(resource['type'], None)

            if not prop:
                raise TerraformComplianceNotImplemented('Encryption property for {} '
                                                        'is not implemented yet.'.format(resource['type']))

            encryption_value = seek_key_in_dict(resource.get('values', {}), encryption_property[resource['type']])

            if len(encryption_value):
                encryption_value = encryption_value[0]

                if type(encryption_value) is dict:
                    encryption_value = encryption_value[encryption_property[resource['type']]]

            if not encryption_value:
                raise Failure('Resource {} does not have encryption enabled ({}={}).'.format(resource['address'],
                                                                                             prop,
                                                                                             encryption_value))

    return True


@then(u'it must {condition:ANY} have {proto:ANY} protocol and port {port} for {cidr:ANY}')
def it_condition_have_proto_protocol_and_port_port_for_cidr(_step_obj, condition, proto, port, cidr):
    proto = str(proto)
    cidr = str(cidr)

    # Set to True only if the condition is 'only'
    condition = condition == 'only'

    # In case we have a range
    if '-' in port:
        if condition:
            raise Failure('"must only" scenario cases must be used either with individual port '
                          'or multiple ports separated with comma.')

        from_port, to_port = port.split('-')
        ports = [from_port, to_port]

    # In case we have comma delimited ports
    elif ',' in port:
        ports = [port for port in port.split(',')]
        from_port = min(ports)
        to_port = max(ports)

    else:
        from_port = to_port = int(port)
        ports = list(set([str(from_port), str(to_port)]))

    from_port = int(from_port) if int(from_port) > 0 else 1
    to_port = int(to_port) if int(to_port) > 0 else 1
    ports[0] = ports[0] if int(ports[0]) > 0 else '1'

    looking_for = dict(proto=proto,
                       from_port=int(from_port),
                       to_port=int(to_port),
                       ports=ports,
                       cidr=cidr)

    for security_group in _step_obj.context.stash:
        check_sg_rules(plan_data=security_group['values'][0],
                       security_group=looking_for,
                       condition=condition)

    return True


@when(u'I {action_type:ANY} them')
def i_action_them(_step_obj, action_type):
    if action_type == "count":

        # WARNING: Only case where we set stash as a dictionary, instead of a list.
        _step_obj.context.stash = {"values": len(_step_obj.context.stash)}
    else:
        raise TerraformComplianceNotImplemented("Invalid action_type in the scenario: {}".format(action_type))


@then(u'I expect the result is {operator:ANY} than {number:d}')
def i_expect_the_result_is_operator_than_number(_step_obj, operator, number):
    # TODO: Maybe iterate over the stash if it is a list and do the execution per each member ?
    value = int(_step_obj.context.stash.get('values', 0))

    if operator == "more":
        assert value > number, "{} is not more than {}".format(value, number)
    elif operator == "more and equal":
        assert value >= number, "{} is not more and equal than {}".format(value, number)
    elif operator == "less":
        assert value < number, "{} is not less than {}".format(value, number)
    elif operator == "less and equal":
        assert value <= number, "{} is not less and equal than {}".format(value, number)
    else:
        raise TerraformComplianceNotImplemented('Invalid operator: {}'.format(operator))


@step(u'its value {condition:ANY} match the "{search_regex}" regex')
def its_value_condition_match_the_search_regex_regex(_step_obj, condition, search_regex, _stash=None):
    def fail(condition):
        text = 'matches' if condition == 'must not' else 'does not match'
        raise Failure('{} property in {} {} {} with {} regex. '
                      'It is set to {}.'.format(_step_obj.context.property_name,
                                                _step_obj.context.name,
                                                _step_obj.context.type,
                                                text,
                                                regex,
                                                values))

    regex = r'{}'.format(search_regex)
    values = _step_obj.context.stash if _stash is None else _stash

    if type(values) is str or type(values) is int or type(values) is bool:
        matches = re.match(regex, str(values), flags=re.IGNORECASE)

        if (condition == 'must' and matches is None) or (condition == "must not" and matches is not None):
            fail(condition)

    elif type(values) is list:
        for value in values:
            its_value_condition_match_the_search_regex_regex(_step_obj, condition, search_regex, value)

    elif type(values) is dict:
        if values.get('values') is not None:
            values = its_value_condition_match_the_search_regex_regex(_step_obj,
                                                                      condition,
                                                                      search_regex,
                                                                      values['values'])
        else:
            values = seek_regex_key_in_dict_values(values, _step_obj.context.property_name, search_regex)

        if (condition == 'must' and values == []) or (condition == "must not" and values != []):
            fail(condition)
