from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Connect_Web.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # messages.success(request, ' this is a test message')
    return render(request, 'index.html')
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your form has been sent successfully.")
        
    return render(request, 'contact.html')

def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)
        
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            redirect(request, 'login.html')
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
