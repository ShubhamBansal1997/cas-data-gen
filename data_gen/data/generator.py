import random

from ..kafka.meta import get_form_meta, get_case_meta
from ..kafka import topics
from ..kafka.producer import ChangeProducer

from .locations import get_all_locations
from .growth_monitoring import get_random_growth_monitoring_form
from .person_case import get_random_mother_case
from .util import DataUnit, SeedValues


def generate_data(count):
    print('generating {} items!'.format(count))


    producer = ChangeProducer('localhost:9092')

    locations = get_all_locations()
    location_randomizer = random.Random("location")
    for i in range(count):
        location = location_randomizer.choice(locations)
        data_generator = DataGenerator(location)
        for data_unit in data_generator.get_data():
            producer.send_change(data_unit.topic, data_unit.data)

    producer.producer.flush()
    print('done!')


class DataGenerator:

    def __init__(self, location_dict):
        self.seed_values = SeedValues(location_dict)

    def get_data(self):
        yield DataUnit(topics.FORM_TOPIC, get_form_meta(get_random_growth_monitoring_form(self.seed_values)))
        yield DataUnit(topics.CASE_TOPIC, get_case_meta(get_random_mother_case(self.seed_values)))
