from django.contrib import admin
from .models import Show

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'venue', 'city')
    list_filter = ('city',)
    search_fields = ('venue', 'city',)
