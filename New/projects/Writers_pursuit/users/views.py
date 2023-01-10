from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            return render(request, "users/login.html",{"value":1,"username":username})
        else:
            return render(request,'users/register.html',{'form':form,"value":1})
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html',{'form':form,"value":0})

def login(request):
    return render(request,"users/login.html",{"value":0})