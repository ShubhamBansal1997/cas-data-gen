import json

from data_gen.data.util import get_template


def get_random_household_case(seed_values):
    template = get_template('household-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    formatted_case = template_string % {
        'hh_case_id': seed_values.case_ids.household,
        'user_id': seed_values.location.get_user_id(),
        'owner_id': seed_values.location.get_owner_id(),
    }
    return json.loads(formatted_case)
