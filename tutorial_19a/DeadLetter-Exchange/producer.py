"""
################
    DeadLetter Implementation
#################
"""

import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.exchange_declare(
    exchange='mainexchange',
    exchange_type=ExchangeType.direct,
)

message = "This message will expire..."

channel.basic_publish(exchange='mainexchange', routing_key='test', body=message) # routing_key = queue name
print(f"Message sent: ${message}")
connection.close()

