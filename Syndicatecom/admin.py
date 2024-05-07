from django.contrib import admin
from .models import Show
from django import forms

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'venue', 'city', 'address')  # Include 'address' in the list display
    list_filter = ('city',)
    search_fields = ('venue', 'city',)


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['date', 'venue', 'city', 'address', 'description', 'flyer']
