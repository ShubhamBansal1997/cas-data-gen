import json

from data_gen.data import randomizers
from data_gen.data.util import get_template


def get_random_mother_case(seed_values):
    template = get_template('mother-person-case.json')
    return randomize_template_values(template, seed_values)


def get_random_child_case(seed_values):
    template = get_template('child-person-case.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    context = {
        'name': randomizers.get_next_child_name(seed_values.random_instance),
    }
    context.update(seed_values.get_context())
    formatted_case = template_string % context
    return json.loads(formatted_case)
