from django.urls import path

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

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("create/", hello.views.create, name="create"),
    path("edituser/", hello.views.edituser, name="edituser"),
    path("map/", hello.views.map, name="map"),
    path("signin/", hello.views.signin, name="signin")
]
