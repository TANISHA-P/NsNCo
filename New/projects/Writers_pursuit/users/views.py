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
    # curr_user = user
    # , {"user_img" : Profile.objects.get(user = user)}
    return render(request,'users/profile.html')

# def adminAccess(request):
#     if request.user.is_superuser:
        