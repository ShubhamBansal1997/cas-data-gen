from datetime import datetime

from ..randomizers import DATE_FORMAT_STRING
from .base import DataGenTestBase


class TestCaseDates(DataGenTestBase):

    def test_adds(self):
        adds = []
        for i in range(5):
            data_generator = self.get_next_data_generator()
            ccs_record_case = data_generator.get_mother_ccs_record_case()
            add_string = ccs_record_case['case_json']['add']
            add = datetime.strptime(add_string, DATE_FORMAT_STRING)
            self.assertTrue(add not in adds)
            adds.append(add)


