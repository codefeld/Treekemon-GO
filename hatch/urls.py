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
    path("map/", woodland.views.map_trees, name="map"),
    path("scan/", woodland.views.scan_trees, name="scan"),
    path("tree/<id>", woodland.views.detail_trees, name="tree"),
    path("random/", woodland.views.random_trees, name="random")
]
