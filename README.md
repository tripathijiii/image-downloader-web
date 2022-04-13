# IMAGE DOWNLOADER
# OverView
This is an online image downloader that can download N number of images of given keyword from the internet zip it and send it to your email.

<img width="638" alt="Screenshot 2022-04-13 at 5 29 59 PM" src="https://user-images.githubusercontent.com/60423130/163175392-b4bb7072-9a5a-4c2e-a5c8-08bd7761c49d.png">

Fill in this fields and Voila! a mail with given number of images will be waiting for you !!!

# ChromeDriver
This is an image downloader using django and chromedriver, while using this please change the chromedriver file to the one that is compatible to your version of chrome.
and also paste the complete path of your chromedriver in the task.py

This uses celery and redis, so install both of them before using this downloader


# REDIS
first you can install redis by $ brew install redis
then start redis using $ brew services start redis
redis will start, to check you can type redis-cli ping.  you should recieve PING
this is for mac

for windows you can install redis directly from https://redis.io/download
then run the redis.cli 


# CELERY
celery can be installed by using pip3/pip install celery
and then use it in the folder using terminal line : $ celery -A Q2 worker


# EMAIL

this has used smtp so fo you to use your own email id just go to the emailing.py and change the sender mail to your mail id and password to your password


# you are good to go after that 

just run python3 manage.py runserver
