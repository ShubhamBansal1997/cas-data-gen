
from .base import DataGenTestBase


class TestCaseRelationships(DataGenTestBase):

    def test_bp_form(self):
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and not data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(7, len(data))
                ccs_record_case = data[2]
                bp_form_data = data[3:6]
                for bp_form in bp_form_data:
                    self.assertEqual(ccs_record_case.data['document']['case_id'],
                                     data_generator.seed_values.case_ids.pregnant_ccs_record)
                    self.assertEqual(ccs_record_case.data['document']['case_id'],
                                     bp_form.data['document']['form']['case_load_ccs_record0']['case']['@case_id'])
                    self.assertNotEqual(
                        '%(form_id)s',
                        bp_form.data['document']['form_id']
                    )
                    self.assertEqual(
                      bp_form.data['document']['received_on'],
                      bp_form.data['document']['form']['meta']['timeEnd'],
                    )

                bp1, bp2, bp3 = bp_form_data

                self.assertTrue(
                    bp1.data['document']['form']['meta']['timeEnd'] < bp2.data['document']['form']['meta']['timeEnd']
                )
                self.assertTrue(
                    bp2.data['document']['form']['meta']['timeEnd'] < bp3.data['document']['form']['meta']['timeEnd']
                )
                break


