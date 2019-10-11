from .util import iter_fixture


def get_all_locations():
    return [Location(loc_dict) for loc_dict in iter_fixture('locations-short.csv')]


class Location:
    def __init__(self, location_dict):
        self._location_dict = location_dict


    def get_owner_id(self):
        return self._location_dict["center_id"]

    def get_user_id(self):
        return self._location_dict["center_id"]

    def get_username(self):
        return self._location_dict["center_name"]
