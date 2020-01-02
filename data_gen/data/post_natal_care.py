import json

from data_gen.data.randomizers import get_next_uuid, get_next_yes_no
from data_gen.data.util import get_template


def get_random_pnc_form(seed_values):
    template = get_template('forms/post-natal-case-form.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    form_context = {
        'submission_time': seed_values.context['pnc1_date'],
        'form_id': get_next_uuid(seed_values.random_instance),
        'random_yes_no': get_next_yes_no(seed_values.random_instance)
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
