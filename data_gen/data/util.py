import csv
import os
from collections import namedtuple
from datetime import timedelta, datetime

from faker import Faker

from . import randomizers

DataUnit = namedtuple('DataUnit', ['topic', 'data'])
CaseIds = namedtuple('CaseIds', [
    'household', 'mother_person', 'pregnant_person', 'child_person', 'child_health',
    'pregnant_ccs_record', 'ccs_record',
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
            edd = randomizers.get_next_edd(self.random_instance)
            lmp = edd - timedelta(days=280)  # 280 = gestational age
            bp1_date = lmp + timedelta(days=90)
            bp2_date = lmp + timedelta(days=180)
            bp3_date = lmp + timedelta(days=230)
            modified_date = datetime.now()
            # Need to be fix
            # As of now it will take a random date from the next 360 days as per the lmp
            random_date = lmp + timedelta(days=randomizers.get_nextInt(self.random_instance) * 36)
            opened_on = lmp - timedelta(days=10)
            pnc1_date = lmp + timedelta(days=300)
            # server_modified_on is actually the latest datetime when the case
            # is updated for raw data we are assuming this to be bp3_date
            self._context = {
                'household_case_id': self.case_ids.household,
                'mother_person_case_id': self.case_ids.mother_person,
                'child_person_case_id': self.case_ids.child_person,
                'pregnant_person_case_id': self.case_ids.pregnant_person,
                'ccs_record_case_id': self.case_ids.ccs_record,
                'pregnant_ccs_record_case_id': self.case_ids.pregnant_ccs_record,
                'child_health_case_id': self.case_ids.child_health,
                'user_id': self.location.get_user_id(),
                'owner_id': self.location.get_owner_id(),
                'pregnant_name': self.fake.name_female(),
                'mother_name': self.fake.name_female(),
                'child_name': self.fake.name(),
                'husband_name': self.fake.name_male(),
                'mother_phone_number': randomizers.get_next_phone_number(self.random_instance),
                'updated_phone_number': randomizers.get_next_phone_number(self.random_instance),
                'add': randomizers.get_next_date(self.random_instance).strftime(randomizers.DATE_FORMAT_STRING),
                'edd': edd.strftime(randomizers.DATE_FORMAT_STRING),
                'lmp': lmp.strftime(randomizers.DATE_FORMAT_STRING),
                'server_modified_on': datetime_to_string(bp3_date),
                'raw_server_modified_on': bp3_date,
                'bp1_date': datetime_to_string(bp1_date),
                'bp2_date': datetime_to_string(bp2_date),
                'bp3_date': datetime_to_string(bp3_date),
                'pnc1_date': datetime_to_string(pnc1_date),
                'child_birth_location': randomizers.get_next_child_birth_location(self.random_instance),
                'preg_order': randomizers.get_nextInt(self.random_instance),
                'date_death': random_date.strftime(randomizers.DATE_FORMAT_STRING),
                'last_date_thr': random_date.strftime(randomizers.DATE_FORMAT_STRING),
                'num_anc_complete': int(self.random_instance.random() * 4),
                'num_pnc_visits': int(self.random_instance.random() * 4),
                'opened_on': datetime_to_string(opened_on),
                'random_yes_no': randomizers.get_next_yes_no(self.random_instance),
                'closed': randomizers.get_next_bool_value(self.random_instance),
                'migration_status': randomizers.get_random_migration_status(self.random_instance),
                'delivery_nature': randomizers.get_random_delivery_nature(self.random_instance)
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


def datetime_to_string(dt):
    return f'{dt.isoformat()}Z'
