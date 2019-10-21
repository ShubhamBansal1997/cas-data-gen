import random
from unittest import TestCase

from ..generator import DataGenerator
from ..locations import get_all_locations


class DataGenTestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.random_instance = random.Random('unit-tests')
        cls.locations = get_all_locations()

    @classmethod
    def get_next_data_generator(cls):
        location = cls.random_instance.choice(cls.locations)
        return DataGenerator(cls.random_instance, location)
