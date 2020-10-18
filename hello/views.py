from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.views import generic

from .forms import RegisterForm

from .models import Greeting, Post, User



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
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = RegisterForm(request.POST, instance=request.user)
#         profile_form = RegisterForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = RegisterForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


def home(request):
    return render(request, "home.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.sqlite3.html", {"greetings": greetings})

def create(request):
    # if request.method == "POST":
    #     form = CreatePost(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #     return redirect("/home")
    # else:
    #     form = RegisterForm()
    #
    # return render("create.html", {"form": form})
    return render(request, "create.html")

def map(request):
    return render(request, "map.html")

def post_detail(request, post_id):
    return HttpResponse("Post %s." % post_id)

def event_detail(request, event_id):
    return HttpResponse("Event %s." % event_id)

class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the latest published posts."""
        return Post.objects.order_by('-created_date')

