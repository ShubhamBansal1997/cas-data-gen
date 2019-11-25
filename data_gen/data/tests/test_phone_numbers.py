from data_gen.data.tests.base import DataGenTestBase


class TestPhoneNumbers(DataGenTestBase):
    def test_override_phone_number_pregnant(self):
        while True:
            data_generator = self.get_next_data_generator()
            if data_generator.is_pregnant and data_generator.change_phone_number:
                data = list(data_generator.get_data())
                self.assertEqual(5, len(data))
                initial_person = data[1]
                updated_person = data[3]
                self.assertEqual(initial_person.data['document']['case_id'],
                                 updated_person.data['document']['case_id'])
                if (initial_person.data['document']['case_json']['contact_phone_number']
                        or updated_person.data['document']['case_json']['contact_phone_number']):
                    self.assertNotEqual(initial_person.data['document']['case_json']['contact_phone_number'],
                                        updated_person.data['document']['case_json']['contact_phone_number'])
                    break


