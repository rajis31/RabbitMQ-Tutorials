"""
################
    Direct / Token Exchange
#################
"""

import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Payments Service: Receieved new message: {body}")


connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue            = channel.queue_declare(queue="", exclusive=True) # idempotent 
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='paymentsonly')
channel.basic_consume(
    queue=queue.method.queue, 
    auto_ack=True, 
    on_message_callback=on_message_received
)

print("Consumer started")
channel.start_consuming()