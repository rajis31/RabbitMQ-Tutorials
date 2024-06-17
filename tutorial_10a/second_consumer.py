"""
################
    A pub / sub model
#################
"""

import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Consumer 2: Receieved new message: {body}")


connection_params =  pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

"""_summary_
    # idempotent 
    # exclusive = True means queue will be deleted after connection is closed
"""
queue = channel.queue_declare(queue="", exclusive=True) 
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Consumer 2 started")
channel.start_consuming()