from django.shortcuts import render, redirect
from . import models
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "loginregister/index.html")

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    confirm = request.POST['confirm']
    registered = models.User.objects.register(request, first_name, last_name, email, password, confirm)
    if (registered):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        query = models.User(first_name = first_name, last_name = last_name, email = email, password_hash = hashed)
        query.save()
        context = {
            'name' : first_name,
            'message' : "Successfully registered!"
        }
        return render(request, "loginregister/success.html", context)
    else:
        return redirect("/")

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = models.User.objects.all().get(email = email)
    if bcrypt.hashpw(password.encode(), user.password_hash.encode()) == user.password_hash.encode():
        context = {
            'name' : user.first_name,
            'message' : "Successfully logged in!"
        }
        return render(request, "loginregister/success.html", context)
    else:
        messages.error(request, "Unable to log in!")
        return redirect("/")
