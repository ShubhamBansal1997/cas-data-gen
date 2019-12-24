import json
import datetime

from data_gen.data.randomizers import get_next_uuid, get_next_yes_no, get_next_datetime_modified
from data_gen.data.util import get_template


def get_random_pnc_form(seed_values):
    template = get_template('forms/post-natal-case-form.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    random_generator = seed_values.random_instance
    datetime_modified_datetime = get_next_datetime_modified(random_generator)
    form_context = {
        'submission_time': datetime.datetime.strftime(datetime_modified_datetime, "%Y-%m-%d"),
        'form_id': get_next_uuid(seed_values.random_instance),
        'random_yes_no': get_next_yes_no(seed_values.random_instance)
    }
    form_context.update(seed_values.context)
    formatted_case = template_string % form_context
    return json.loads(formatted_case)
