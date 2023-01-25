import time
from utils import create_schema
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from kafka_config import sasl_conf, TOPIC
from mongo_config import MongodbInsert


def consume_data_to_db():
    schema_str = create_schema()
    json_deserializer = JSONDeserializer(schema_str)

    consumer_conf = sasl_conf()
    consumer_conf.update({
        'group.id': 'group1',
        'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([TOPIC])

    mongodb = MongodbInsert()
    records = []
    x = 0
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            record = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
            if x % 10 == 0:
                print(x, record)

            if record is not None:
                records.append(record)
                if x % 5000 == 0:
                    mongodb.insert_many(records=records)
                    records = []
            x = x + 1
        except KeyboardInterrupt:
            break

    consumer.close()


if __name__ == '__main__':
    consume_data_to_db()
