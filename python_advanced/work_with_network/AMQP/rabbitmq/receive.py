import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):  # Standard function
    print(f" [x] Received {body}")


channel.basic_consume(callback, queue='hello', no_ack=True)  # Create instance consume

channel.start_consuming()  # Start infinity listen
