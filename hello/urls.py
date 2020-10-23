from django.conf.urls import url
from django.urls import path, include
from . import views
from . import forms

app_name = 'hello'

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"home/", views.HomeView.as_view(), name="home"),
    path(r"db/", views.db, name="db"),
    path(r"register/", views.register, name="register"),
    path(r"account/", views.edit_profile, name="account"),
    path(r"db.sqlite3/", views.db, name="db.sqlite3"),
    path(r"create/", views.create_post, name="create"),
    path(r"map/", views.map, name="map"),
    # ex: /post/5/
    #edit_profile
    path(r'post/<int:question_id>/', views.post_detail, name='post_detail'),
    path(r'event/<int:question_id>/', views.event_detail, name='event_detail'),
]
