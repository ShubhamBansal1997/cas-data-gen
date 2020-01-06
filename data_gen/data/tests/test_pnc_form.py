from .base import DataGenTestBase


class TestPNCForm(DataGenTestBase):

    def test_pnc_form(self):
        yes_no_options = ['yes', 'no']  # used to check bool values
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and not data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(10, len(data))
                ccs_record_case = data[2]
                pnc_form_data = data[6]
                # redundant case test
                # note: try to avoid in further test cases
                # self.assertEqual(ccs_record_case.data['document']['case_id'],
                # data_generator.seed_values.case_ids.pregnant_ccs_record)
                self.assertEqual(ccs_record_case.data['document']['case_id'],
                                 pnc_form_data.data['document']['form']['case_load_ccs_record0']['case']['@case_id'])
                self.assertNotEqual(
                    '%(form_id)s',
                    pnc_form_data.data['document']['form_id']
                )
                self.assertEqual(
                    pnc_form_data.data['document']['received_on'],
                    pnc_form_data.data['document']['form']['meta']['timeEnd'],
                )
                # bool fields here
                self.assertIn(pnc_form_data.data['document']['form']['child']['item']['is_ebf'], yes_no_options)
                break
