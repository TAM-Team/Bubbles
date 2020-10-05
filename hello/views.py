from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Greeting, Post


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-created_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))


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

def signin(request):
    return render(request, "signin.html")

def create_user(request):
    #try:
    return render(request, "edituser.html")

def edituser(request):
    return render(request, "edituser.html")

