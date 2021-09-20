import django
django.setup()
from Q5.models import database,queue
from download_images import download_images
from Q5.emailing import sendmail
from django.utils import timezone

i = queue.objects.all()
for j in i:
    download_images.main(["-q",str(j.keyword),"-l",str(j.number),"-c","chromedriver.exe"])
    sendmail(j.email,j.keyword)
    b= database(keyword = j.keyword,number = j.number,email = j.email,time = timezone.now() )
    b.save()
    j.delete()