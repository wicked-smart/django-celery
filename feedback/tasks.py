from celery import shared_task
from time import sleep


@shared_task()
def add(x,y):
    sleep(30)
    return x+y

@shared_task()
def subtract(x,y):
    sleep(30)
    return (x-y)


