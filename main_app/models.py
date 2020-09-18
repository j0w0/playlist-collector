from django.db import models
from django.urls import reverse

# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'playlist_id': self.id})
