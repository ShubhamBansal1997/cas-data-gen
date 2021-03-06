import json

from data_gen.data.randomizers import get_next_uuid, get_next_yes_no
from data_gen.data.util import get_template


def get_random_bp_form(seed_values, visit_number):
    template = get_template('forms/bp/bp{}.json'.format(visit_number))
    return randomize_template_values(template, seed_values, visit_number)


def randomize_template_values(template_string, seed_values, visit_number):
    seed_value_key = 'bp{}_date'.format(visit_number)
    form_context = {
        'form_id': get_next_uuid(seed_values.random_instance),
        'submission_time': seed_values.context[seed_value_key],
        'random_yes_no': get_next_yes_no(seed_values.random_instance),
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
