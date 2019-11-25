import json

from data_gen.data import randomizers
from data_gen.data.util import get_template


def get_random_pregnant_case(seed_values, override_context=None):
    template = get_template('preg-woman-person-case.json')
    return randomize_template_values(template, seed_values, override_context)


def get_random_mother_case(seed_values):
    template = get_template('mother-person-case.json')
    return randomize_template_values(template, seed_values)


def get_random_child_case(seed_values):
    template = get_template('child-person-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values, override_context=None):
    context = seed_values.context
    if override_context:
        print('ovewriting: {}'.format(override_context))
        context.update(override_context)
    formatted_case = template_string % seed_values.context
    return json.loads(formatted_case)
