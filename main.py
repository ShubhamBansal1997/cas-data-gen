import argparse

from data_gen.data.growth_monitoring import get_random_growth_monitoring_form
from data_gen.data.person_case import get_random_mother_case
from data_gen.kafka import topics
from data_gen.kafka.meta import get_case_meta, get_form_meta
from data_gen.kafka.producer import ChangeProducer


def generate_data(count):
    print('generating {} items!'.format(count))
    producer = ChangeProducer('localhost:9092')
    for i in range(count):
        producer.send_change(topics.FORM_TOPIC, get_form_meta(get_random_growth_monitoring_form()))
        producer.send_change(topics.CASE_TOPIC, get_case_meta(get_random_mother_case()))
    producer.producer.flush()
    print('done!')


parser = argparse.ArgumentParser(description='Generate fake CAS data.')
parser.add_argument('multiplier', type=int,
                    help='Number of items of each data type to generate')

args = parser.parse_args()

generate_data(args.multiplier)
