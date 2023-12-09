from celery import shared_task
from time import sleep

@shared_task(name="Subtraction_task")
def sub(x, y):
    sleep(10)
    return x - y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id 

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key 