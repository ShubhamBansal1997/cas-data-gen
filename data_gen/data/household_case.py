import json

from data_gen.data.util import get_template


def get_random_household_case(seed_values):
    template = get_template('household-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    formatted_case = template_string % seed_values.context
    return json.loads(formatted_case)
