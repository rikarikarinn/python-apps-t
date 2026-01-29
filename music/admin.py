from django.contrib import admin
from .models import Genre, Artist, Track, Playlist, PlaylistItem


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "artist", "genre")
    list_filter = ("genre", "artist")
    search_fields = ("title",)


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 1


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    inlines = [PlaylistItemInline]
