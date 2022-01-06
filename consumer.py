from kafka import KafkaConsumer
# consume earliest available messages
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=True)

consumer = KafkaConsumer('OLA_MUNDO', group_id='console-consumer-27716', bootstrap_servers=['localhost:9092'])

for message in consumer:
    message_str = message.value.decode('utf-8')
    print(message_str)