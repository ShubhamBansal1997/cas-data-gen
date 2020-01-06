from .base import DataGenTestBase
from data_gen.data.randomizers import STILL_LIVE_CASES


class TestDeliveryForm(DataGenTestBase):

    def test_delivery_form(self):
        yes_no_options = ['yes', 'no']
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and not data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(10, len(data))
                ccs_record_case = data[2]
                delivery_form_data = data[8]
                # redundant case test
                # note: try to avoid in further test cases
                # self.assertEqual(ccs_record_case.data['document']['case_id'],
                #                  data_generator.seed_values.case_ids.pregnant_ccs_record)
                self.assertEqual(ccs_record_case.data['document']['case_id'],
                                 delivery_form_data.data['document']['form']['case_load_ccs_record0']['case']['@case_id'])
                self.assertNotEqual(
                    '%(form_id)s',
                    delivery_form_data.data['document']['form_id']
                )
                self.assertEqual(
                    delivery_form_data.data['document']['received_on'],
                    delivery_form_data.data['document']['form']['meta']['timeEnd'],
                )
                self.assertIn(delivery_form_data.data['document']['form']['child']
                              ['breastfed_within_first_hour'], yes_no_options)
                self.assertIn(delivery_form_data.data['document']['form']
                              ['child']['still_live_birth'], STILL_LIVE_CASES)
                self.assertTrue(delivery_form_data.data['document']['form']['days_visit_late'].isdigit())
                self.assertTrue(delivery_form_data.data['document']['form']['num_children_del'].isdigit())
                self.assertIn(delivery_form_data.data['document']['form']
                              ['unscheduled_visit'], ['0', '1'])

                break
