from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.views import generic

from .forms import RegisterForm

from .models import Greeting, Post


# Created views

def index(request):
    return render(request, "index.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


def home(request):
    return render(request, "home.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def create(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render("registration/register.html", {"form": form})
    #return render(request, "create.html")

def map(request):
    return render(request, "map.html")

def post_detail(request, post_id):
    return HttpResponse("Post %s." % post_id)

class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the latest published posts."""
        return Post.objects.order_by('-created_date')

