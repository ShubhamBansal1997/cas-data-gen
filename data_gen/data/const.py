import random
import datetime

RANDOM_FORM1 = random.Random("form1")
RANDOM_FORM2 = random.Random("form2")
DATE_FORMAT_STRING = '%Y-%m-%d'
ACTIVITY_LIST = ["prayer_hygiene", "conversation", "cognitive",
                 "physical_outdoor", "arts_crafts", "language", "packup"]
MEAL_SERVED_LIST = ["cooked_served_hot", "cooked_served_cold",
                    "packed_served_hot", "packed_served_cold", "not_served"]
START_DATETIME = datetime.datetime(2018, 7, 1)
END_DATETIME = datetime.datetime(2019, 7, 1)
LOCATIONS_FILE = "locations.csv"
CASE_LIST = []
ANEMIA_STATES = ["", "severe", "moderate", "normal"]
MAX_VALUE = 32767
ANC_BLOOD_PRESSURE_STATES = ["", "normal", "high", "not_measured"]
CHILD_BIRTH_LOCATIONS = ["hospital", "home"]
MIGRATION_STATUS = ["migrated", ""]
DELIVERY_NATURES = ["", "vaginal", "caesarean", "instrumental"]
YES_NO_STATES = ["yes", "no"]