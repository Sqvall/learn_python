import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # Open connection
channel = connection.channel()  # Create channel
channel.queue_declare(queue='hello')  # Create queue

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')  # Send message
print(" [x] Sent 'Hello World!'")

channel.close()  # Close connection
