import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

load_dotenv()

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def list_trees(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "list.html")

def map_trees(request):
    context = {
        "google_maps_api_key": os.getenv("GOOGLE_MAPS_API_KEY"),
        "trees": [
            {
                "lat": 34.5,
                "lng": -86.4,
                "url": "/",
                "name": "Fabulous Cheese Tree"
            },
            {
                "lat": 34.4,
                "lng": -86.5,
                "url": "/",
                "name": "Fabulous Money Tree"
            }
        ]
    }
    return render(request, "map.html", context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
