from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.template.context_processors import csrf
from django.views import generic
import os
import pprint
import pdb


pp = pprint.PrettyPrinter(indent=4)


from pygments import console

from .forms import RegisterForm, CustomUserChangeForm, CreatePostForm, CreateEventForm

from .models import Greeting, Post, User, Event



# Created views

def index(request):
    return render(request, "initial.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST, response.FILES)

        if form.is_valid():
            form.save()
            return redirect("hello:home")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form": form})


def home(request):
    return render(request, "home.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    users = User()
    users.save()
    users = User.objects.all()
    return render(request, "db.html", {
        "greetings": greetings,
        "users": users
    })

def map(request):
    return render(request, "map.html")

def post_detail(request, post_id):
    return HttpResponse("Post %s." % post_id)

def event_detail(request, event_id):
    return HttpResponse("Event %s." % event_id)

class HomeView(generic.ListView):
    template_name = 'posts.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the latest published posts."""
        return Post.objects.order_by('-created_date')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! You have successfully updated your account!")
            return redirect('hello:account')
    else:
        form = CustomUserChangeForm(instance=request.user)
    args = {}
    args.update(csrf(request))
    args['user_form'] = form
    return render(request, 'registration/profile.html', args)

@login_required
def create_post(request):
    if request.method == 'POST':
        create_post_form = CreatePostForm(request.POST, user=request.user)
        create_post_form.poster = request.user
        if create_post_form.is_valid():
            create_post_form.save()
            return redirect('hello:home')
    else:
        create_post_form = CreatePostForm(user=request.user)
    args = {}
    args.update(csrf(request))
    args['create_post_form'] = create_post_form
    return render(request, 'create_post.html', args)

@login_required
def create_event(request):
    if request.method == 'POST':
        create_event_form = CreateEventForm(request.POST, user=request.user)
        create_event_form.poster = request.user
        if create_event_form.is_valid():
            create_event_form.save()
            return redirect('hello:home')
    else:
        create_event_form = CreateEventForm(user=request.user)
    args = {}
    args.update(csrf(request))
    args['create_event_form'] = create_event_form
    return render(request, 'create_event.html', args)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def event_detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'event_detail.html', {'event': event})


