from .util import iter_fixture


def get_all_locations():
    return list(iter_fixture('locations-short.csv'))
