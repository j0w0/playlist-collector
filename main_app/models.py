from django.db import models
from django.urls import reverse

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=100)
    # artist should be own data entity
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})

    # use Field.choices for genre?
    # https://git.generalassemb.ly/SEI-CC/SEI-CC-9/blob/master/work/w08/d3/03-04-django-one-to-many-models/django-one-to-many-models.md#fieldchoices
    # https://git.generalassemb.ly/SEI-CC/SEI-CC-9/blob/master/work/w08/d3/03-04-django-one-to-many-models/django-one-to-many-models.md#fix-the-meal-select


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'playlist_id': self.id})

    def comment_count(self):
        return self.comment_set.count()


class Comment(models.Model):
    date = models.DateField(
        'Comment Date'
    )
    comment = models.TextField(max_length=250)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment left on {self.date} - {self.comment}"

    class Meta:
        ordering = ['-date']
