from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def create(request):
    return render(request, "create.html")

def map(request):
    return render(request, "map.html")


def signin(request):
    return render(request, "signin.html")

def create_user(request):
    #try:
    return render(request, "edituser.html")

def edituser(request):
    return render(request, "edituser.html")

