from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Client

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account is registered succesfully!')
            return redirect('app1-home')
        else:
            messages.error(request,f'Error while creating Account! Please try again')
            return redirect('app1-register')
    else:
        form = UserCreationForm()
        return render(request,"app1/register.html",{'form':form})