from datetime import datetime

from ..randomizers import DATE_FORMAT_STRING
from .base import DataGenTestBase


class TestPregnantAndMother(DataGenTestBase):

    def test_is_pregnant(self):
        pregnant_count = mother_count = 0
        for i in range(100):
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant:
                pregnant_count += 1
            else:
                mother_count += 1

        # just make sure we generate a few of each, and that mother makes up the majority
        self.assertTrue(pregnant_count > 10)
        self.assertTrue(mother_count > 50)

    def test_pregnant_types(self):
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant:
                data = list(data_generator.get_data())
                self.assertEqual(4, len(data))
                break

    def test_mother_types(self):
        while True:
            data_generator = self.get_next_data_generator()
            if not data_generator.is_pregnant:
                data = list(data_generator.get_data())
                self.assertEqual(6, len(data))
                break

    def test_edds_are_random_in_future(self):
        edds = []
        now = datetime.utcnow()
        for i in range(5):
            data_generator = self.get_next_data_generator()
            ccs_record_case = data_generator.get_pregnant_ccs_record_case()
            edd_string = ccs_record_case['case_json']['edd']
            edd = datetime.strptime(edd_string, DATE_FORMAT_STRING)
            print("edd is {}".format(edd))
            self.assertTrue(edd not in edds)
            self.assertTrue(edd >= now)
            edds.append(edd)

    def test_adds_are_random_and_in_past(self):
        adds = []
        now = datetime.utcnow()
        for i in range(5):
            data_generator = self.get_next_data_generator()
            ccs_record_case = data_generator.get_mother_ccs_record_case()
            add_string = ccs_record_case['case_json']['add']
            add = datetime.strptime(add_string, DATE_FORMAT_STRING)
            self.assertTrue(add not in adds)
            self.assertTrue(add <= now)
            adds.append(add)


