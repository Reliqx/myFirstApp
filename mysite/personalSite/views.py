from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from personalSite.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import logout




def user(request):
    return render(request, 'personal/user.html')

def logout_view(request):
    logout(request)
    args = {'logoutmsg': 'sucessful logout!'}
    return render(request, 'personal/home.html',args)
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html' ,{'content': ['if you would like to contact me, please email me', 'relq09@gmail.com']})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/register')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'personal/registration_form.html', args)

def profile(request):
    args = {'user':request.user}
    return render(request,'personal/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/user/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'personal/edit_profile.html',args)
        
        
                

                

    
