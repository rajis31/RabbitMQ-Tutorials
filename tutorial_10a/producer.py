"""
################
    A pub / sub model
#################
"""

import pika
from pika.exchange_type import ExchangeType

connection_params =  pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "Hello I want to broadcast this message"
channel.basic_publish(exchange='pubsub', routing_key='', body=message) # routing_key = queue name
print(f"Message sent: ${message}")
connection.close()
