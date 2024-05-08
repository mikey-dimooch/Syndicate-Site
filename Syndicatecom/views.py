from django.shortcuts import render
from .models import Show
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, "home.html")

def tour(request):
    return render(request, 'tour.html')

def band(request):
    return render(request, 'band.html')

def music(request):
    return render(request, 'music.html')

def merch(request):
    return render(request, 'merch.html')

def contact(request):
    return render(request, 'contact.html')


def tour(request):
    upcoming_shows = Show.objects.filter(date__gte=timezone.now()).order_by('date')
    past_shows = Show.objects.filter(date__lt=timezone.now()).order_by('-date')

    return render(request, 'tour.html', {
        'upcoming_shows': upcoming_shows,
        'past_shows': past_shows
    })

