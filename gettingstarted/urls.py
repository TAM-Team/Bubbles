from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


app_name = 'hello'

urlpatterns = [
    path(r"", hello.views.index, name="index"),
    path(r"db/", hello.views.db, name="db"),
    path(r"admin/", admin.site.urls),
    path(r"create/", hello.views.create, name="create"),
    path(r"edituser/", hello.views.edituser, name="edituser"),
    path(r"map/", hello.views.map, name="map"),
    path(r"account/", include('django.contrib.auth.urls'), name="account"),
    path(r"account/login", include('django.contrib.auth.urls'), name="login"),
    # ex: /post/5/
    path(r'post/<int:question_id>/', hello.views.post_detail, name='post_detail'),
]
