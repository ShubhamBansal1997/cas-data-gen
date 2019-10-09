import json
import random

from data_gen.data import randomizers
from data_gen.data.util import get_template


def get_random_mother_case():
    template = get_template('mother-person-case.json')
    return randomize_template_values(template, random.Random("mother"))


def randomize_template_values(template_string, random_generator):
    formatted_case = template_string % {
        'case_id': randomizers.get_next_uuid(random_generator),
        'hh_case_id': randomizers.get_next_uuid(random_generator),
        'name': randomizers.get_next_child_name(random_generator),
    }
    return json.loads(formatted_case)
