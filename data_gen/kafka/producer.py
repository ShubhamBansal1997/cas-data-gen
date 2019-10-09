import json

from kafka import KafkaProducer


class ChangeProducer(object):
    # heavily inspired by CommCare HQ's ChangeProducer class

    def __init__(self, servers):
        self._producer = KafkaProducer(
            bootstrap_servers=servers,
            client_id="datagen-producer",
            retries=3,
            acks=1,
            key_serializer=lambda key: str(key).encode()
        )

    def send_change(self, topic, change_meta):
        message = change_meta.to_json()
        message_json_dump = json.dumps(message).encode('utf-8')
        self._producer.send(topic, message_json_dump, key=change_meta.document_id)
