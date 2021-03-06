import random
from datetime import timedelta

from data_gen.data.birth_preparedness import get_random_bp_form
from ..kafka.meta import get_form_meta, get_case_meta
from ..kafka import topics
from ..kafka.producer import ChangeProducer

from .ccs_record_case import get_random_mother_ccs_record_case, get_random_pregnant_ccs_record_case
from .child_health_case import get_random_child_health_case
from .growth_monitoring import get_random_growth_monitoring_form
from .household_case import get_random_household_case
from .locations import get_all_locations
from .randomizers import get_next_uuid
from .person_case import get_random_mother_case, get_random_child_case, get_random_pregnant_case
from .util import DataUnit, SeedValues, CaseIds, datetime_to_string


def generate_data(count):
    print('generating {} items!'.format(count))
    producer = ChangeProducer('localhost:9092')
    locations = get_all_locations()
    # random_instance = random.Random("cas-data-generator-{}".format(count))
    random_instance = random.Random()
    for i in range(count):
        location = random_instance.choice(locations)
        data_generator = DataGenerator(random_instance, location)
        for data_unit in data_generator.get_data():
            producer.send_change(data_unit.topic, data_unit.data)

    producer.producer.flush()
    print('done!')


class DataGenerator:

    def __init__(self, random_instance, location):
        self.random_instance = random_instance
        # one in four should be pregnant, the rest should be mothers
        self.is_pregnant = random_instance.random() > .75
        # one in ten should change their phone number
        self.change_phone_number = random_instance.random() > .9
        case_ids = CaseIds(
            household=get_next_uuid(self.random_instance),
            mother_person=get_next_uuid(self.random_instance),
            pregnant_person=get_next_uuid(self.random_instance),
            child_person=get_next_uuid(self.random_instance),
            child_health=get_next_uuid(self.random_instance),
            pregnant_ccs_record=get_next_uuid(self.random_instance),
            ccs_record=get_next_uuid(self.random_instance),
        )
        self.seed_values = SeedValues(
            random_instance=self.random_instance,
            location=location,
            case_ids=case_ids
        )

    def get_data(self):
        yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_household_case()))
        if self.is_pregnant:
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_pregnant_case()))
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_pregnant_ccs_record_case()))
            if self.change_phone_number:
                yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_pregnant_case_new_number()))

            # forms
            for i in range(3):
                yield DataUnit(topics.FORM_TOPIC, get_form_meta(self.get_bp_form(i + 1)))

        else:
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_mother_case()))
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_mother_ccs_record_case()))
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_child_case()))
            yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_child_health_case()))
            if self.change_phone_number:
                yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_mother_case_new_number()))

        yield DataUnit(topics.FORM_TOPIC, get_form_meta(self.get_growth_monitoring_form()))

    # cases
    def get_household_case(self):
        return get_random_household_case(self.seed_values)

    def get_mother_case(self):
        return get_random_mother_case(self.seed_values)

    def get_mother_case_new_number(self):
        return get_random_mother_case(self.seed_values, override_context={
            'mother_phone_number': self.seed_values.context['updated_phone_number'],
            'server_modified_on': datetime_to_string(
                self.seed_values.context['raw_server_modified_on'] + timedelta(days=30)
            ),
        })

    def get_mother_ccs_record_case(self):
        return get_random_mother_ccs_record_case(self.seed_values)

    def get_child_case(self):
        return get_random_child_case(self.seed_values)

    def get_child_health_case(self):
        return get_random_child_health_case(self.seed_values)


    def get_pregnant_case(self):
        return get_random_pregnant_case(self.seed_values)

    def get_pregnant_case_new_number(self):
        return get_random_pregnant_case(self.seed_values, override_context={
            'mother_phone_number': self.seed_values.context['updated_phone_number'],
            'server_modified_on': datetime_to_string(
                self.seed_values.context['raw_server_modified_on'] + timedelta(days=30)
            ),
        })

    def get_pregnant_ccs_record_case(self):
        return get_random_pregnant_ccs_record_case(self.seed_values)

    # forms
    def get_bp_form(self, visit_number):
        return get_random_bp_form(self.seed_values, visit_number)

    def get_growth_monitoring_form(self):
        return get_random_growth_monitoring_form(self.seed_values)
