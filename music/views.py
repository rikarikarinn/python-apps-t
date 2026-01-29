import random
from django.shortcuts import render
from .models import Track


def index(request):
    return HttpResponse("music app 動いてる！")


def recommend_random(request):
    tracks = list(Track.objects.all())

    if not tracks:
        return render(request, "music/recommend.html", {
            "track": None
        })

    track = random.choice(tracks)

    return render(request, "music/recommend.html", {
        "track": track
    })
