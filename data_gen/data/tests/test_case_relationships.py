import random
from unittest import TestCase

from ..generator import DataGenerator
from ..locations import get_all_locations


class TestCaseRelationships(TestCase):

    def test_basic(self):
        random_instance = random.Random('unit-tests')
        locations = get_all_locations()
        location = random_instance.choice(locations)
        data_generator = DataGenerator(random_instance, location)

        hh_case = data_generator.get_household_case()
        mother_case = data_generator.get_mother_case()
        ccs_record_case = data_generator.get_ccs_record_case()
        child_case = data_generator.get_child_case()
        child_health_case = data_generator.get_child_health_case()
        # mother case parent is household
        self.assertEqual(hh_case['case_id'], mother_case['indices'][0]['referenced_id'])
        self.assertEqual('parent', mother_case['indices'][0]['identifier'])

        # ccs record case parent is mother
        self.assertEqual(mother_case['case_id'], ccs_record_case['indices'][0]['referenced_id'])
        self.assertEqual('parent', ccs_record_case['indices'][0]['identifier'])

        # child case parent is household
        self.assertEqual(hh_case['case_id'], child_case['indices'][1]['referenced_id'])
        self.assertEqual('parent', child_case['indices'][1]['identifier'])

        # child case "mother" index is mother
        self.assertEqual(mother_case['case_id'], child_case['indices'][0]['referenced_id'])
        self.assertEqual('mother', child_case['indices'][0]['identifier'])

        # child health case parent index is child
        self.assertEqual(child_case['case_id'], child_health_case['indices'][0]['referenced_id'])
        self.assertEqual('parent', child_health_case['indices'][0]['identifier'])
