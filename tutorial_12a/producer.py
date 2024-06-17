"""
################
    Direct / Token Exchange
#################
"""

import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)
message = "This is a stupid payment"

channel.basic_publish(exchange='mytopicexchange', routing_key='data', body=message) # routing_key = queue name
print(f"Message sent: ${message}")
connection.close()

