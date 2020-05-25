from django.shortcuts import render
from django.http import HttpResponse 
from . import forms
from . models import Chat
from django.contrib.auth.decorators import login_required
from .dataGenerator.python_message_converter import getData
import os
# Create your views here.


@login_required(login_url="/accounts/login")
def add(request):
    if request.method == 'POST':
        form = forms.Insert(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            user1 = request.POST.get('username1')
            user2 = request.POST.get('username2')

            getid=form.instance.id
            status = getData(user1,user2,getid)
            if status:
                return render(request,"chat/download.html")
            #return HttpResponse("domea")
    else:
        form = forms.Insert()
        return render(request,'chat/adding.html',{'form':form})
    # patel_mansi_07_09_
    # eswar._.rajpurohit
    
@login_required(login_url="/accounts/login")
def download(request):
    
    with open("./message.txt",'r') as msg:
        response = HttpResponse(msg.read(),content_type="application/msword")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename("./message.txt")

        try:
            return response
        except:
            return Http404
    return render(request,"chat/download.html")