import csv
import os
from collections import namedtuple


DataUnit = namedtuple('DataUnit', ['topic', 'data'])
SeedValues = namedtuple('SeedValues', ['location'])


def get_template(template_name):
    template_filename = os.path.join(os.path.dirname(__file__), 'templates', template_name)
    with open(template_filename, "r") as f:
        template_string = f.read()

    return template_string


def iter_fixture(fixture_name):
    template_filename = os.path.join(os.path.dirname(__file__), 'fixtures', fixture_name)
    with open(template_filename, "r") as f:
        reader = csv.DictReader(f)
        yield from reader


