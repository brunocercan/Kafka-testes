from kafka import KafkaProducer
from kafka.errors import KafkaError


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# Asynchronous by default
message = 'Ola Mundo'

message_byte = str.encode(message)

future = producer.send('OLA_MUNDO', message_byte)

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)