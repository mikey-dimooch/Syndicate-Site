from django.db import models
from django.utils import timezone

class Show(models.Model):
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)  # Added address field
    description = models.TextField(blank=True, null=True)
    flyer = models.ImageField(upload_to='flyers/', blank=True, null=True)

    def is_past(self):
        return self.date < timezone.now()

    def __str__(self):
        return f"{self.venue} - {self.city} on {self.date.strftime('%Y-%m-%d')}"


