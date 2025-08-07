from django.shortcuts import render

# Create your views here.
def view_dashboard(request):
    return render(request,"customer/dashboard.html")


def password_change(request):
    return render(request,"customer/password_change.html")