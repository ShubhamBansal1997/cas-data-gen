from .growth_monitoring import get_random_growth_monitoring_form
from .person_case import get_random_mother_case
from data_gen.kafka.meta import get_form_meta, get_case_meta
from ..kafka import topics
from ..kafka.producer import ChangeProducer


def generate_data(count):
    print('generating {} items!'.format(count))
    producer = ChangeProducer('localhost:9092')
    for i in range(count):
        producer.send_change(topics.FORM_TOPIC, get_form_meta(get_random_growth_monitoring_form()))
        producer.send_change(topics.CASE_TOPIC, get_case_meta(get_random_mother_case()))
    producer.producer.flush()
    print('done!')
