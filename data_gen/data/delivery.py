import json


from data_gen.data.randomizers import get_next_uuid, get_next_yes_no, get_still_live_cases, get_nextInt, get_next_bool_value, get_next_child_birth_location
from data_gen.data.util import get_template


def get_random_delivery_form(seed_values):
    template = get_template('forms/delivery-form.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    form_context = {
        'form_id': get_next_uuid(seed_values.random_instance),
        'submission_time': seed_values.context['add'],
        'random_yes_no': get_next_yes_no(seed_values.random_instance),
        'still_live_birth': get_still_live_cases(seed_values.random_instance),
        'days_visit_late': get_nextInt(seed_values.random_instance) * 10,
        'num_children_del': get_nextInt(seed_values.random_instance),
        'unscheduled_visit': int(get_next_bool_value(seed_values.random_instance)),
        'child_birth_location': get_next_child_birth_location(seed_values.random_instance)
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
