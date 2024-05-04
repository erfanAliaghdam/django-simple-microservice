import pika, json, os
from services import MailService

mail_service = MailService()

RABBITMQ_Q = os.environ.get("RABBITMQ_Q")

params = pika.URLParameters(RABBITMQ_Q)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="mail")


def callback(ch, method, properties, body):
    print("Received in Consumer")
    data = json.loads(body)
    print(data)

    if properties.content_type == "user_registered":
        print("User registeration triggered.")
        mail_service.send_mail()

    if properties.content_type == "user_new_device_login":
        print("User new device login triggered.")
        mail_service.send_mail()

channel.basic_consume(queue="mail", on_message_callback=callback, auto_ack=True)

print("Started Consuming ... .")

channel.start_consuming()

channel.close()
