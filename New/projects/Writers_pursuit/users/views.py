from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            curruser = User.objects.get(username = username)
            prof = Profile()
            prof.user = curruser
            prof.save()
            messages.success(request, f'Account Created Succesfully for {username}!')
            return redirect('blog-home')
        else:
            messages.error(request,f'Error while creating Account! Please try again')
            return render(request,'users/register.html')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html',{"form":form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

# def adminAccess(request):
#     if request.user.is_superuser:

def another_person_profile(request, data):
    the_other_user = User.objects.filter(username = data).first()
    if(the_other_user):
        print(the_other_user.email)
        return render(request,'users/other_profile.html',{"otheruser":the_other_user})
    else:
        return render(request,'users/no_user.html')