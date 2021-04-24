import os
import json
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

load_dotenv()

with open("woodland/data/champions.json", "r") as f:
    tree_data = f.read()

trees = json.loads(tree_data)

# Create your views here.
def index(request):
    return render(request, "index.html")

def list_trees(request):
    context = {
        "trees": trees["trees"]
    }
    return render(request, "list.html", context)

def map_trees(request):
    context = {
        "google_maps_api_key": os.getenv("GOOGLE_MAPS_API_KEY"),
        "trees": trees["trees"]
    }
    return render(request, "map.html", context)

def detail_trees(request, id):
    print("id = %s" % id)
    for tree in trees["trees"]:
        if tree["id"] == int(id):
            context = {
                "tree": tree,
                "image_height": tree["height"] + 20
            }
            return render(request, "tree.html", context)
    raise Http404("This tree is not in our database. :(")

def scan_trees(request):
    context = {
        "trees": trees["trees"]
    }
    return render(request, "scan.html", context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
