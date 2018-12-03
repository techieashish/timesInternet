from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.core.mail import EmailMessage


@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def send_mail():
    email = EmailMessage('Category Email', 'Hey', to=['naveen.kumar1@timesinternet.in'])
    email.send()