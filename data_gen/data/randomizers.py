import datetime
import random
import uuid


RANDOM_EXAMPLE = random.Random("a")
RANDOM_FORM1 = random.Random("form1")
RANDOM_FORM2 = random.Random("form2")
DATE_FORMAT_STRING = '%Y-%m-%d'
ACTIVITY_LIST = ["prayer_hygiene", "conversation", "cognitive", "physical_outdoor", "arts_crafts", "language", "packup"]
MEAL_SERVED_LIST = ["cooked_served_hot", "cooked_served_cold", "packed_served_hot", "packed_served_cold", "not_served"]
START_DATETIME = datetime.datetime(2018, 7, 1)
END_DATETIME = datetime.datetime(2019, 7, 1)
LOCATIONS_FILE = "locations.csv"
CASE_LIST = []


### Functions to get specific variables within templates
def get_next_uuid(randomObj):
    return str(uuid.UUID(int = randomObj.getrandbits(128)))

def get_nextInt(randomObj):
    return int(randomObj.random() * 10)

def get_next_activity(randomObj):
    return randomObj.sample(ACTIVITY_LIST,int(randomObj.random() * len(ACTIVITY_LIST)))

def get_next_meal_served(randomObj):
    return randomObj.sample(MEAL_SERVED_LIST,int(randomObj.random() * len(MEAL_SERVED_LIST)))

def get_next_yes_no(randomObj):
    if randomObj.random() < .5:
        return "yes"
    else:
        return "no"

def get_next_child_id(randomObj):
    ## TO-DO: Fix this
    return get_next_uuid(randomObj)

def get_next_datetime_modified(randomObj, start=START_DATETIME, end=END_DATETIME):
    delta_microseconds = (end - start).days * 24 * 60 * 60 * 1000000
    randomObj.random()
    return start + datetime.timedelta(microseconds=randomObj.random()*delta_microseconds)

def get_next_date(randomObj):
    return get_next_datetime_modified(randomObj)

def get_next_edd(random_instance):
    start = datetime.datetime.utcnow()
    end = start + datetime.timedelta(days=240)  # pregnancy due dates are expected sometime in the next ~8 months
    print("start {} end {}".format(start, end))
    return get_next_datetime_modified(random_instance, start, end)


def get_next_gps_location(randomObj):
    latitude = str(int(randomObj.random() * 180) - 90)
    longitude = str(int(randomObj.random() * 360) - 180)
    return latitude + " " + longitude + " 0.0 25.55"

def get_next_device_id(randomObj):
    return str(int(randomObj.random() * 1000000000000000))

def get_next_ip(randomObj):
    place1 = str(int(randomObj.random() * 256))
    place2 = str(int(randomObj.random() * 256))
    place3 = str(int(randomObj.random() * 256))
    place4 = str(int(randomObj.random() * 256))
    return place1 + "." + place2 + "." + place3 + "." + place4

def get_next_child_name(randomObj):
    ## TO-DO: Fix this
    return get_next_uuid(randomObj)

def get_next_wfa(randomObj):
    return round(randomObj.random() * 20 - 10, 4)

def get_next_zscore(randomObj):
    return round(randomObj.random() * 6-3, 2)

def get_next_age_days(randomObj):
    return int(randomObj.random() * 1000)

def get_next_sex(randomObj):
    return "M" if randomObj.random() < 0.5 else "F"

def get_next_location_dict(locationCycle):
    nextRow = locationCycle.next()
    return {"location_id": nextRow[0], "name": nextRow[2]}

def get_random_location_dict(randomObj):
    return {
        'location_id': get_next_uuid(randomObj),
        'name': get_next_child_name(randomObj),
    }


def get_next_phone_number(random_instance):
    """
    Returns a phone number like: +91XXXXNNNNNN or an empty string with 5% probability
    """
    if random_instance.random() < .95:
        return f'+91{random_instance.randint(1000000000, 9999999999)}'
    else:
        return ''
