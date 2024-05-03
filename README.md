# Django Simple Microservice

![Screenshot 1403-02-14 at 20 38 58](https://github.com/erfanAliaghdam/django-simple-microservice/assets/80113382/864d798f-d16f-454a-a672-6743a59a689b)



# How to Run Each Service?

## Step 1: Navigate to the Service Directory

```bash
cd <service_name>
```

Replace `<service_name>` with the name of the service you want to run.

## Step 2: Build and Run Docker Containers

```bash
docker-compose up --build -d
```

This command will build the Docker images if they don't exist and start the containers in detached mode.

## Step 3: RabbitMQ Configuration

Before running each service, you need to initialize the RabbitMQ URL inside the respective service's environment file.

### User Service

Navigate to `userService/rabbitmq/local/` directory and create or edit the `.env.local` file.

### Logger Service

Navigate to `loggerService/rabbitmq/local/` directory and create or edit the `.env.local` file.

### Mail Service

Navigate to `mailService/rabbitmq/local/` directory and create or edit the `.env.local` file.

### Example RabbitMQ URL Initialization

Inside each `.env.local` file, add the RabbitMQ URL in the following format:

```plaintext
RABBITMQ_Q=amqp://...
```

## Testing REST API Endpoints

You can use the `.HTTP` files inside the `requests` folder inside `userService` to test the REST API endpoints.
