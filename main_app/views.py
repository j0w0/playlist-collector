from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Playlist, Song
from .forms import CommentForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def playlists_index(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/index.html', {'playlists': playlists})


def playlists_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    available_songs = Song.objects.exclude(id__in=playlist.songs.all())
    comment_form = CommentForm()
    return render(request, 'playlists/detail.html', {
        'playlist': playlist,
        'comment_form': comment_form,
        'songs': available_songs,
    })


class PlaylistCreate(CreateView):
    model = Playlist
    fields = '__all__'
    success_url = '/playlists/'


class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = '__all__'


class PlaylistDelete(DeleteView):
    model = Playlist
    fields = '__all__'
    success_url = '/playlists/'


def add_comment(request, playlist_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.playlist_id = playlist_id
        new_comment.save()
    return redirect('detail', playlist_id=playlist_id)


def assoc_song(request, playlist_id, song_id):
    Playlist.objects.get(id=playlist_id).songs.add(song_id)
    return redirect('detail', playlist_id=playlist_id)


def unassoc_song(request, playlist_id, song_id):
    Playlist.objects.get(id=playlist_id).songs.remove(song_id)
    return redirect('detail', playlist_id=playlist_id)


class SongList(ListView):
    model = Song


class SongDetail(DetailView):
    model = Song


class SongCreate(CreateView):
    model = Song
    fields = '__all__'


class SongUpdate(UpdateView):
    model = Song
    fields = '__all__'


class SongDelete(DeleteView):
    model = Song
    success_url = '/songs/'
