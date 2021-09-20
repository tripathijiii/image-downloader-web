from celery import shared_task
from time import sleep
from .models import *
from download_images import download_images
from .emailing import sendmail
from django.utils import timezone

@shared_task
def worktodo(keyword,number,email):
    download_images.main(["-q",str(keyword),"-l",str(number),"-c","chromedriver"])
    sendmail(email,keyword)