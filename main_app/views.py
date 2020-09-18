from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


class Playlist:
    def __init__(self, title, description):
        self.title = title
        self.description = description


playlists = [
    Playlist('House', '😎'),
    Playlist('TripHop', 'Nice.'),
    Playlist('90s Mix', 'Nineties.'),
    Playlist('Cumbia', 'Good music.')
]


def home(request):
    return HttpResponse('<h1>Hello!</h1>')


def about(request):
    return render(request, 'about.html')


def playlists_index(request):
    return render(request, 'playlists/index.html', {'playlists': playlists})
