import json
import datetime

from . import randomizers
from .util import get_template


def get_random_growth_monitoring_form(seed_values):
    template = get_template('growth-monitoring-form.json')
    return randomize_template_values(template, seed_values)


def randomize_template_values(template_string, seed_values):
    random_generator = seed_values.random_instance
    wfa = randomizers.get_next_wfa(random_generator)
    wfa_pos = abs(wfa)
    weight = randomizers.get_nextInt(random_generator)
    zscore = randomizers.get_next_zscore(random_generator)
    zscore_wfa = zscore * 3
    zscore_icon = "red" if zscore_wfa < 3 else "yellow" if zscore_wfa < 2 else "green"
    nutrition_status = "severely underweight" if zscore_wfa < 3 else "moderately underweight" if zscore_wfa < 2 else "normal"
    datetime_modified_datetime = randomizers.get_next_datetime_modified(random_generator)
    datetime_modified = datetime.datetime.strftime(datetime_modified_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
    date_modified = datetime.datetime.strftime(datetime_modified_datetime, "%Y-%m-%d")
    age_days = randomizers.get_next_age_days(random_generator)
    age_weeks = age_days / 7.0
    age_weeks_rounded = int(age_weeks)
    age_months = age_days / 30.25
    age_months_rounded = int(age_months)
    age_dob = datetime.datetime.strftime(datetime_modified_datetime - datetime.timedelta(days = age_days),"%Y-%m-%d")
    yes_no = randomizers.get_next_yes_no(random_generator)
    sex = randomizers.get_next_sex(random_generator)
    form_id = randomizers.get_next_uuid(random_generator)
    formXML_id = randomizers.get_next_uuid(random_generator)
    deviceID = randomizers.get_next_device_id(random_generator)
    child_name = randomizers.get_next_child_name(random_generator)
    last_sync_token = randomizers.get_next_uuid(random_generator)
    submit_ip = randomizers.get_next_ip(random_generator)

    newForm = template_string % dict(
        wfa=wfa,
        child_id=seed_values.case_ids.child_person,
        weight=weight,
        zscore=zscore,
        zscore_wfa=zscore_wfa,
        zscore_icon=zscore_icon,
        nutrition_status=nutrition_status,
        age_days=age_days,
        age_weeks=age_weeks,
        age_weeks_rounded=age_weeks_rounded,
        age_months=age_months,
        age_months_rounded=age_months_rounded,
        age_dob=age_dob,
        yes_no=yes_no,
        owner_id=seed_values.location.get_owner_id(),
        sex=sex,
        form_id=form_id,
        user_id=seed_values.location.get_user_id(),
        username=seed_values.location.get_username(),
        formXML_id=formXML_id,
        datetime_modified=datetime_modified,
        date_modified=date_modified,
        deviceID=deviceID,
        child_name=child_name,
        wfa_pos=wfa_pos,
        last_sync_token=last_sync_token,
        submit_ip=submit_ip
    )
    return json.loads(newForm)
