import json

from data_gen.data.util import get_template


def get_random_ccs_record_case(seed_values):
    template = get_template('ccs-record-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    formatted_case = template_string % seed_values.get_context()
    return json.loads(formatted_case)