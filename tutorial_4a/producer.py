import pika

connection_params = pika.ConnectionParameters('localhost')
connection        = pika.BlockingConnection(connection_params)
channel           = connection.channel()

channel.queue_declare(queue="letterbox")
message = "Hello this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message) # routing_key = queue name
print(f"Message sent: ${message}")
connection.close()

