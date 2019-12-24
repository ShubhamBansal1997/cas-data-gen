
from .base import DataGenTestBase
from data_gen.data.randomizers import ANEMIA_STATES, MAX_VALUE, ANC_BLOOD_PRESSURE_STATES


class TestCaseRelationships(DataGenTestBase):

    def _get_form_root_property(self, form, property, internal_form='bp1'):
        return form.data['document']['form'][internal_form][property]

    def _get_form_iter_0_property(self, form, property, internal_form='bp1'):
        return form.data['document']['form'][internal_form]['iteration']['item'][0]['filter']['anc_details'][property]

    def test_bp_form(self):
        random_yes_no = ['yes', 'no']  # used to check bool values
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and not data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(8, len(data))
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
                # bool fields here
                self.assertIn(self._get_form_root_property(bp1, 'resting'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'eating_extra'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'bleeding', 'bp2'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'swelling', 'bp2'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'blurred_vision', 'bp2'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'convulsions', 'bp2'), random_yes_no)
                self.assertIn(self._get_form_root_property(bp1, 'rupture', 'bp2'), random_yes_no)
                self.assertIn(self._get_form_iter_0_property(bp1, 'anc_abnormalities'), random_yes_no)
                # switch case fields here
                self.assertIn(self._get_form_root_property(bp1, 'anemia'), ANEMIA_STATES)
                self._get_form_iter_0_property(bp1, 'anc_blood_pressure')
                self.assertIn(self._get_form_iter_0_property(bp1, 'anc_blood_pressure'), ANC_BLOOD_PRESSURE_STATES)
                # range cases
                self.assertGreater(int(self._get_form_iter_0_property(bp1, 'anc_weight')), 0)
                self.assertLess(int(self._get_form_iter_0_property(bp1, 'anc_weight')), MAX_VALUE)
                self.assertGreater(int(self._get_form_iter_0_property(bp1, 'bp_sys')), 0)
                self.assertLess(int(self._get_form_iter_0_property(bp1, 'bp_sys')), MAX_VALUE)
                self.assertGreater(int(self._get_form_iter_0_property(bp1, 'bp_dias')), 0)
                self.assertLess(int(self._get_form_iter_0_property(bp1, 'bp_dias')), MAX_VALUE)
                self.assertGreater(float(self._get_form_iter_0_property(bp1, 'anc_hemoglobin')), 0)
                self.assertLess(float(self._get_form_iter_0_property(bp1, 'anc_hemoglobin')), float(MAX_VALUE))

                break
