from django.urls import path, include
from . import views

app_name = 'hello'

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"db/", views.db, name="db"),
    path(r"create/", views.create, name="create"),
    path(r"edituser/", views.edituser, name="edituser"),
    path(r"map/", views.map, name="map"),
    path(r"account/", include('django.contrib.auth.urls'), name="account"),
    path(r"account/login", include('django.contrib.auth.urls'), name="login"),
    # ex: /post/5/
    path(r'post/<int:question_id>/', views.post_detail, name='post_detail'),
]