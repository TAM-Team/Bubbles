from django.conf.urls import url
from django.urls import path, include
from . import views
from . import forms

app_name = 'hello'

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"home/", views.HomeView.as_view(), name="home"),
    path(r"register/", views.register, name="register"),
    path(r"db.sqlite3/", views.db, name="db.sqlite3"),
    path(r"create/", views.create, name="create"),
    path(r"map/", views.map, name="map"),
    # ex: /post/5/
    path(r'post/<int:question_id>/', views.post_detail, name='post_detail'),
]
