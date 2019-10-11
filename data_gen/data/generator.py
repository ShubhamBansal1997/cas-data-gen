import random

from ..kafka.meta import get_form_meta, get_case_meta
from ..kafka import topics
from ..kafka.producer import ChangeProducer

from .locations import get_all_locations
from .growth_monitoring import get_random_growth_monitoring_form
from .household_case import get_random_household_case
from .randomizers import get_next_uuid
from .person_case import get_random_mother_case, get_random_child_case
from .util import DataUnit, SeedValues, CaseIds


def generate_data(count):
    print('generating {} items!'.format(count))
    producer = ChangeProducer('localhost:9092')
    locations = get_all_locations()
    random_instance = random.Random("cas-data-generator-{}".format(count))
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
        case_ids = CaseIds(
            household=get_next_uuid(self.random_instance),
            mother_person=get_next_uuid(self.random_instance),
            child_person=get_next_uuid(self.random_instance),
        )
        self.seed_values = SeedValues(
            random_instance=self.random_instance,
            location=location,
            case_ids=case_ids
        )

    def get_data(self):
        yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_household_case()))
        yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_mother_case()))
        yield DataUnit(topics.CASE_TOPIC, get_case_meta(self.get_child_case()))
        yield DataUnit(topics.FORM_TOPIC, get_form_meta(self.get_growth_monitoring_form()))


    def get_household_case(self):
        return get_random_household_case(self.seed_values)

    def get_mother_case(self):
        return get_random_mother_case(self.seed_values)

    def get_child_case(self):
        return get_random_child_case(self.seed_values)

    def get_growth_monitoring_form(self):
        return get_random_growth_monitoring_form(self.seed_values)
