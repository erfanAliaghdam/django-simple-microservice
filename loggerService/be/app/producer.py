import pika, json, logging
from django.conf import settings


params = pika.URLParameters(settings.RABBITMQ_Q)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body, routing_key):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key=routing_key,
        body=json.dumps(body),
        properties=properties,
    )
    logging.info(f"Publishing {method} from user service.")
