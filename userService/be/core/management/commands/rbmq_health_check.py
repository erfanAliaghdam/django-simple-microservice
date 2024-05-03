from django.core.management.base import BaseCommand
import pika, os


RABBITMQ_Q = os.environ.get("RABBITMQ_Q")


class Command(BaseCommand):
    help = "Check RabbitMQ health"

    def handle(self, *args, **kwargs):
        health = False
        while health is False:
            try:
                params = pika.URLParameters(RABBITMQ_Q)
                connection = pika.BlockingConnection(params)
                connection.close()

                self.stdout.write(self.style.SUCCESS("RabbitMQ is healthy"))
                health = True
            except pika.exceptions.AMQPError as e:
                self.stdout.write(
                    self.style.ERROR("RabbitMQ health check failed: {}".format(e))
                )
