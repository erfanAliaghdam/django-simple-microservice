from django.core.management.base import BaseCommand
import pika, os, json, ast
from log.services import LogService


class Command(BaseCommand):
    help = "run consumers"

    def handle(self, *args, **kwargs):
        log_service = LogService()

        RABBITMQ_Q = os.environ.get("RABBITMQ_Q")

        params = pika.URLParameters(RABBITMQ_Q)

        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        channel.queue_declare(queue="log")

        def callback(ch, method, properties, body):
            print("Received in Consumer")
            data = json.loads(body)

            if properties.content_type == "user_logged_in":
                print("User loggin triggered.")
                log_service.create_log(
                    user_id=data.get("user_id", None),
                    user_ip=data.get("user_ip", None),
                    user_device=data.get("user_device", None),
                    request_time=data.get("request_time", None),
                    user_email=data.get("user_email", None),
                )

        channel.basic_consume(queue="log", on_message_callback=callback, auto_ack=True)

        print("Started Consuming ... .")

        channel.start_consuming()

        channel.close()
