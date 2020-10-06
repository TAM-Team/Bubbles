from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader

from .models import Greeting, Post


# Create your views here.
def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def create(request):
    return render(request, "create.html")

def map(request):
    return render(request, "map.html")

def post_detail(request, post_id):
    return HttpResponse("Post %s." % post_id)

