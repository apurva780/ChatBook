from django.shortcuts import render
from django.http import HttpResponse 
from . import forms
from . models import Chat
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/accounts/login")
def add(request):
    if request.method == 'POST':
        form = forms.Insert(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #instance = forms.Insert(attach=request.FILES['file'])
            #instance.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponse("completed")
    else:
        form = forms.Insert()
        return render(request,'chat/adding.html',{'form':form})
    