import json

from .randomizers import get_next_uuid, get_nextInt
from .util import get_template


def get_random_thr_form(seed_values):
    template = get_template('forms/thr-form.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    form_context = {
        'submission_time': seed_values.context['thr_date'],
        'form_id': get_next_uuid(seed_values.random_instance),
        'days_ration_given_mother': get_nextInt(seed_values.random_instance)
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
