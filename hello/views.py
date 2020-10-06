from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Greeting, Post


# Create your views here.
def index(request):
    latest_post_list = get_list_or_404(Post, Post.was_created_recently())


    template = loader.get_template('index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    HttpResponse("home.html")

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

