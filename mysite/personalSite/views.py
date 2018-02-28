from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html' ,{'content': ['if you would like to contact me, please email me', 'relq09@gmail.com']})

class UserFormView(View):
    form_class = UserForm
    template_name = 'personal/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form} )
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #creates an object from the form, doesnt save to the database
            user = form.save(commit=False)

            #clean (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #to change pw
            user.set_password(password)
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('personal/home.html')
        return render(request, self.template_name, {'form': form} )

                
                

                

    
