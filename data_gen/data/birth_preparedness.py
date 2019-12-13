import json

from data_gen.data.util import get_template


def get_random_bp_form(seed_values, visit_number):
    template = get_template('forms/bp/bp{}.json'.format(visit_number))
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    formatted_case = template_string % seed_values.context
    return json.loads(formatted_case)
