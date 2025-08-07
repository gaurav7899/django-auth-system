from django.shortcuts import render,redirect
from account.forms import RegistrationForm
from django.contrib import messages
from account.models import User

# email send
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
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
            # print(user.email)
            user.save()
            # send email activation link
            # get pk 
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # genrate token use default_token_generator
            token = default_token_generator.make_token(user)
            activation_link = reverse("activate",kwargs={"uidb64":uidb64,"token":token})
            activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
            send_activation_email(user.email,activation_url)
            messages.success(request,"Registration successfull! Please check your email to activate your account")
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,"account/register.html",{'form':form})

# activation view
def activation_account(request,uidb64,token):
    try:
        # get user pk
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user.is_active:
            messages.warning(request,"This account has been activated")
            return redirect('login')
        
        # check token
        if default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(request,"Your account has been activate successfully!")
            return redirect('login')
        else:
            messages.error(request,"The activation link is invalid or has expired.")
            return redirect('login')
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(request,"Ivalid activation link.")
        return redirect('login')


# login page
def login(request):
    return render(request,"account/login.html")

def logout(request):
    return render(request,"account/activation_email.html")

def password_reset(request):
    return render(request,"account/password_reset.html")

def set_password(request):
    return render(request,"account/password_reset_confirm.html")