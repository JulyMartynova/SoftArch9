# Event-Driven and Pipes-and-Filters System

This project demonstrates two architectures: event-driven using RabbitMQ and pipes-and-filters using queues and processes. The system consists of several services that process messages, filter them, convert them to uppercase, and send emails.

## Project Structure

- `filters/`: Folder containing modules for each service in the pipes-and-filters architecture.
  - `filter_service.py`: Service for filtering messages.
  - `screaming_service.py`: Service for converting messages to uppercase.
  - `publish_service.py`: Service for sending emails.
- `services/`: Folder containing modules for each service in the event-driven architecture.
  - `api_service.py`: Flask API service to send messages to RabbitMQ.
  - `filter_service.py`: Service for filtering messages using RabbitMQ.
  - `screaming_service.py`: Service for converting messages to uppercase using RabbitMQ.
  - `publish_service.py`: Service for sending emails using RabbitMQ.
- `main.py`: Main file to run the pipes-and-filters system.
- `rabbitmq.py`: Main file to run the event-driven system.
- `README.md`: This file.

## Installation

1. **Install Python**: Ensure you have Python 3.6 or higher installed.
2. **Install Dependencies**: Install the required dependencies using pip.

```bash
pip install -r requirements.txt
```
Set up RubbitMQ
```bash
docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
Run rabbitMQ services:
```bash
python rabbitmq.py
```

Run pipes and filters services:
```bash
python pipes_and_filters.py
```

To compare performance metrics, run this command
```bash
python main.py
```









