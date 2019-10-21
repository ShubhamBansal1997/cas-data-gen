import csv
import os
from collections import namedtuple

from faker import Faker

from . import randomizers

DataUnit = namedtuple('DataUnit', ['topic', 'data'])
CaseIds = namedtuple('CaseIds', [
    'household', 'mother_person', 'pregnant_person', 'child_person', 'child_health', 'ccs_record'
])

class SeedValues(namedtuple('SeedValues', ['random_instance', 'location', 'case_ids'])):

    @property
    def fake(self):
        if not hasattr(self, '_fake'):
            self._fake = Faker()
            self._fake.random = self.random_instance
        return self._fake

    @property
    def context(self):
        if not hasattr(self, '_context'):
            self._context = {
                'household_case_id': self.case_ids.household,
                'mother_person_case_id': self.case_ids.mother_person,
                'child_person_case_id': self.case_ids.child_person,
                'ccs_record_case_id': self.case_ids.ccs_record,
                'child_health_case_id': self.case_ids.child_health,
                'user_id': self.location.get_user_id(),
                'owner_id': self.location.get_owner_id(),
                'mother_name': self.fake.name_female(),
                'child_name': self.fake.name(),
                'husband_name': self.fake.name_male(),
                'mother_phone_number': randomizers.get_next_phone_number(self.random_instance),
                'add': randomizers.get_next_date(self.random_instance).strftime(randomizers.DATE_FORMAT_STRING),
            }
        return self._context

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


