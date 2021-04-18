from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import woodland.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", woodland.views.index, name="index"),
    path("list/", woodland.views.list_trees, name="list"),
    path("map/", woodland.views.map_trees, name="map")
]
