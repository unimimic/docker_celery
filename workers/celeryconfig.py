import os

USER = os.environ['RABBITMQ_DEFAULT_USER']
PASS = os.environ['RABBITMQ_DEFAULT_PASS']

# Timezone
timezone = 'Asia/Taipei'

## Broker settings.
broker_url = f'amqp://{USER}:{PASS}@rabbitmq:5672'

## Using the database to store task state and results.
result_backend = f'rpc://{USER}:{PASS}@rabbitmq:5672'

# List of modules to import when the Celery worker starts.
imports = (
    'workers.tasks.tasks_1',
    'workers.tasks.tasks_2',
)
