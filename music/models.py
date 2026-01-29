from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="tracks"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="tracks"
    )

    def __str__(self):
        return f"{self.title} - {self.artist.name}"


from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class PlaylistItem(models.Model):
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE,
        related_name="items"
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name="playlist_items"
    )
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
        unique_together = ("playlist", "track")

    def __str__(self):
        return f"{self.order}: {self.track.title}"
