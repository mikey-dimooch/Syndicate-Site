from django.contrib import admin
from .models import Show
from django import forms
from .models import Album

# Register your models here.
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'venue', 'city', 'state', 'date']
    list_filter = ['venue', 'city', 'state', 'date']
    search_fields = ['event_name', 'venue', 'description']
    fields = ['event_name', 'venue', 'city', 'state', 'date', 'description', 'ticket_link', 'setlist']

admin.site.register(Album)

