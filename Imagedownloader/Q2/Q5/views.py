from django.utils import timezone
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from download_images import download_images
from .emailing import sendmail
from .task import worktodo

from .models import database, queue

# Create your views here.
def homepage(request):
    if request.method=="POST":
        keyword=request.POST.get('name',)
        number=request.POST.get('no',)
        email = request.POST.get('email',)
        a = queue(keyword=keyword,number=number,email=email)
        a.save()
        
        return redirect('thankyou/')

    return render(request,'myapp/index.html')

def thankyou(request):
    list = queue.objects.all()
    worktodo.delay(list[0].keyword,list[0].number,list[0].email)
    b= database(keyword=list[0].keyword,number=list[0].number,email=list[0].email,time=timezone.now())
    b.save()
    list[0].delete()
    return render(request,'myapp/thankou.html')
