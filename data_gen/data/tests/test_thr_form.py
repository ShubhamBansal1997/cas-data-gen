from .base import DataGenTestBase


class TestTHRForm(DataGenTestBase):

    def test_thr_form(self):
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and not data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(10, len(data))
                ccs_record_case = data[2]
                thr_form_data = data[7]
                # redundant case test
                # note: try to avoid in further test cases
                # self.assertEqual(ccs_record_case.data['document']['case_id'],
                #                  data_generator.seed_values.case_ids.pregnant_ccs_record)
                self.assertEqual(ccs_record_case.data['document']['case_id'],
                                 thr_form_data.data['document']['form']['case_load_ccs_record_0']['case']['@case_id'])
                self.assertNotEqual(
                    '%(form_id)s',
                    thr_form_data.data['document']['form_id']
                )
                self.assertEqual(
                    thr_form_data.data['document']['received_on'],
                    thr_form_data.data['document']['form']['meta']['timeEnd'],
                )
                self.assertTrue(thr_form_data.data['document']['form']
                                ['mother_thr']['days_ration_given_mother'].isdigit())
                break
