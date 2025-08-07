from django.shortcuts import render,redirect
from account.forms import RegistrationForm
from django.contrib import messages

# email send
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
# home page --> account

def home(request):
    return render(request,"account/home.html")

# register form page
def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            messages.success(request,"Registration successfull! Please check your email to activate your account")
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,"account/register.html",{'form':form})
# login page
def login(request):
    return render(request,"account/login.html")

def logout(request):
    return render(request,"account/activation_email.html")

def password_reset(request):
    return render(request,"account/password_reset.html")

def set_password(request):
    return render(request,"account/password_reset_confirm.html")