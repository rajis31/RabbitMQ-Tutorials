"""
################
    Competing Consumer Implementation
#################
"""

import pika
import time
import random

def on_message_received(ch, method, properties, body):
    process_time = random.randint(1,6)
    print(f"Receieved new message: {body}, will take {process_time} to process")
    time.sleep(process_time)
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("Finished processing the message")



connection_params =  pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.queue_declare(queue="letterbox") # idempotent 
channel.basic_qos(prefetch_count=1) # Set prefetch count = 1
channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print("Consumer started")
channel.start_consuming()