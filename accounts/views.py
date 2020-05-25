from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            #return HttpResponse("created")
            return redirect('chatting:add')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form' : form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('chatting:add')
    
    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})

def show(request):
    return render(request,'accounts/show.html')

def logout_view(request):
    #if request.method == 'POST':
        logout(request)   #current login user
        return redirect('accounts:show')
        #return HttpResponse("logout")

def start(request):
    return render(request,"accounts/getstarted.html")