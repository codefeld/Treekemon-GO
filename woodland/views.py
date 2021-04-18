import os
import json
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

load_dotenv()

with open("woodland/data/trees.json", "r") as f:
    tree_data = f.read()

trees = json.loads(tree_data)

print("trees: " + str(trees))

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


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
