from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'hello'

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"/", views.index, name="index"),
    path(r"home/", views.home, name="home"),
    path(r"db/", views.db, name="db"),
    path(r"create/", views.create, name="create"),
    path(r"map/", views.map, name="map"),
    # ex: /post/5/
    path(r'post/<int:question_id>/', views.post_detail, name='post_detail'),
]
