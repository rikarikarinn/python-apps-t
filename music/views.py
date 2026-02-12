from django.shortcuts import render
from .models import Track
import random

def recommend(request):
    tracks = list(Track.objects.all())
    track = random.choice(tracks) if tracks else None
    return render(request, 'music/recommend.html', {'track': track})
