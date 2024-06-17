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
    name = models.CharField(max_length=200)
    cover_url = models.ImageField(upload_to='album_covers/')
    recorded_at = models.CharField(max_length=200, null=True, blank=True)
    credits = models.TextField(null=True, blank=True)
    spotify_url = models.URLField(max_length=200, null=True, blank=True)
    apple_music_url = models.URLField(max_length=200, null=True, blank=True)
    youtube_url = models.URLField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)  # Ensure this field is present

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Image {}".format(self.id)
