import json

from data_gen.data.randomizers import get_next_uuid, get_next_yes_no, get_anemia_state, get_int, get_anc_blood_pressure_state, get_decimal, get_nextInt
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
        'anemia': get_anemia_state(seed_values.random_instance),
        'random_int': get_int(seed_values.random_instance),
        'anc_blood_pressure': get_anc_blood_pressure_state(seed_values.random_instance),
        'random_decimal': get_decimal(seed_values.random_instance),
        'ifa_last_seven_days': get_nextInt(seed_values.random_instance)
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
