import csv
import os
from collections import namedtuple


DataUnit = namedtuple('DataUnit', ['topic', 'data'])
CaseIds = namedtuple('CaseIds', ['household', 'mother_person', 'child_person', 'child_health', 'ccs_record'])

class SeedValues(namedtuple('SeedValues', ['random_instance', 'location', 'case_ids'])):

    def get_context(self):
        return {
            'household_case_id': self.case_ids.household,
            'mother_person_case_id': self.case_ids.mother_person,
            'child_person_case_id': self.case_ids.child_person,
            'ccs_record_case_id': self.case_ids.ccs_record,
            'child_health_case_id': self.case_ids.child_health,
            'user_id': self.location.get_user_id(),
            'owner_id': self.location.get_owner_id(),
        }


def get_template(template_name):
    template_filename = os.path.join(os.path.dirname(__file__), 'templates', template_name)
    with open(template_filename, "r") as f:
        template_string = f.read()

    return template_string


def iter_fixture(fixture_name):
    template_filename = os.path.join(os.path.dirname(__file__), 'fixtures', fixture_name)
    with open(template_filename, "r") as f:
        reader = csv.DictReader(f)
        yield from reader


