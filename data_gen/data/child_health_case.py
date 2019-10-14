import json

from data_gen.data import randomizers
from data_gen.data.util import get_template


def get_random_child_health_case(seed_values):
    template = get_template('child-health-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    formatted_case = template_string % {
        'mother_person_case_id': seed_values.case_ids.mother_person,
        'household_case_id': seed_values.case_ids.household,
        'child_person_case_id': seed_values.case_ids.household,
        'child_health_case_id': seed_values.case_ids.child_health,
        'user_id': seed_values.location.get_user_id(),
        'owner_id': seed_values.location.get_owner_id(),
        'name': randomizers.get_next_child_name(seed_values.random_instance),
    }
    return json.loads(formatted_case)
