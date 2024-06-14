from django.db import models
from django.utils import timezone

class Show(models.Model):
    event_name = models.CharField(max_length=255)
    venue = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    ticket_link = models.URLField(blank=True, null=True)
    setlist = models.TextField(blank=True, null=True)  # Storing each song separated by new lines

    def __str__(self):
        return f"{self.event_name} at {self.venue} on {self.date.strftime('%Y-%m-%d')}"
    


class Album(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='album_covers/')
    release_date = models.DateField()
    spotify_link = models.URLField(blank=True)
    apple_music_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    credits = models.TextField()

    def __str__(self):
        return self.title

state = models.CharField(max_length=100, default='Unknown')
