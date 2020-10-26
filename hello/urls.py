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
    # View database to make sure adding user was working
    path(r"db.sqlite3/", views.db, name="db.sqlite3"),

    path(r"create/", views.create_post, name="create"),
    path(r"map/", views.map, name="map"),
    # ex: /post/5/
    path(r'post/<int:post_id>/', views.post_detail, name='post_detail'),
    # ex: /event/5/
    path(r'event/<int:event_id>/', views.event_detail, name='event_detail'),
]
