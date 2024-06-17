import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"Receieved new message: {body}")


connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.exchange_declare(exchange="secondexchange", exchange_type=ExchangeType.fanout)
channel.queue_declare(queue="letterbox") # idempotent 
channel.queue_bind('letterbox', 'secondexchange')
channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

print("Consumer started")
channel.start_consuming()