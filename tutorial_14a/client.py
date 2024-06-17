"""
################
    Request Response Implementation
#################
"""

import pika
import uuid
import time
import random

def on_reply_message_received(ch, method, properties, body):
    print(f"Reply received: {body}")

connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()
reply_queue       = channel.queue_declare(queue="", exclusive=True)
channel.basic_consume(
        queue=reply_queue.method.queue, 
        auto_ack=True, 
        on_message_callback=on_reply_message_received
)
channel.queue_declare(queue='request-queue')


message           = "Can I request a reply?"
corrId            = str(uuid.uuid4())
print(f"Sending request: {corrId}")

channel.basic_publish(
    exchange='', 
    routing_key='request-queue', 
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=corrId
    ),
    body=message
)

print(f"Starting Client")
channel.start_consuming()

