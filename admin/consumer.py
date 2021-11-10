import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "admin.settings")
django.setup()
import json

import pika





from products.models import Products

params = pika.URLParameters("amqps://vfchomdw:1a3bInD6To-Z7MOlDXamu0u8cbY3hYkR@hornet.rmq.cloudamqp.com/vfchomdw")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Received in admin")
    print(body)
    id = json.loads(body)
    print(id)
    product = Products.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()

    print("Like Received")



channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=False)

print("Launched")

channel.start_consuming()
channel.close()
