from celery import Celery

# Broker URL format: 'amqp://username:password@host:port/virtual_host'
broker_url = 'amqp://tosingh:peranofo54@172.161.146.165:5672/rabbit'

# Create Celery instance
celery_app = Celery('app', broker=broker_url)


# Autodiscover tasks
celery_app.autodiscover_tasks(['app'], related_name='tasks', force=True)
