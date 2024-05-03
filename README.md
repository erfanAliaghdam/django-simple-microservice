# Django Simple Microservice

![Screenshot 1403-02-14 at 20 38 58](https://github.com/erfanAliaghdam/django-simple-microservice/assets/80113382/864d798f-d16f-454a-a672-6743a59a689b)


# How to run each service?
> cd < service_name >

> docker-compose up --build -d


Note: initialize your rabbitmq url inside :

> user service : userService/rabbitmq/local/.env.local

> logger service : loggerService/rabbitmq/local/.env.local

> mail service : mailService/rabbitmq/local/.env.local
