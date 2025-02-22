"""
################
    Request Response Implementation
#################
"""

import pika
import uuid

def on_request_message_received(ch, method, properties, body):
    print(f"Request received: {properties.correlation_id}")
    ch.basic_publish(
        exchange='', 
        routing_key=properties.reply_to,
        body=f"Hey its your reply to {properties.correlation_id}"
    )

connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()
reply_queue       = channel.queue_declare(queue="request-queue")
print(reply_queue.method.queue)
channel.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_request_message_received)
print("Starting Server")
channel.start_consuming()







