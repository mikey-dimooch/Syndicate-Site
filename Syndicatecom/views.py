from django.shortcuts import render, redirect
from .models import Show
from django.utils import timezone
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import GalleryImage
from .models import Album

# Create your views here.
def home(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'home.html', {'gallery_images': gallery_images})

def tour(request):
    return render(request, 'tour.html')

def band(request):
    return render(request, 'band.html')

def music(request):
    return render(request, 'music.html')

def merch(request):
    return render(request, 'merch.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Construct the email body
        email_body = f"Message from {name} ({email}):\n\n{message}"

        # send an email
        send_mail(
            'New Message From ' + name, # subject
            email_body, # message
            email, # from email (who's filling out the form)
            ['syndicatethrash@gmail.com'], # to email (band email)
        )


        return render(request, 'contact.html', {'name':name})
    else:
        return render(request, 'contact.html')


def tour(request):
    upcoming_shows = Show.objects.filter(date__gte=timezone.now()).order_by('date')
    past_shows = Show.objects.filter(date__lt=timezone.now()).order_by('-date')
    return render(request, 'tour.html', {
        'upcoming_shows': upcoming_shows,
        'past_shows': past_shows
    })


def music(request):
    albums = Album.objects.all()
    return render(request, 'music.html', {'albums': albums})

def album_details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        release_date = album.release_date.strftime('%B %d, %Y') if album.release_date else 'N/A'
    except Exception as e:
        release_date = 'Error: ' + str(e)
    
    data = {
        'name': album.name,
        'cover_url': album.cover_url.url,
        'recorded_at': album.recorded_at,
        'credits': album.credits,
        'spotify_url': album.spotify_url,
        'apple_music_url': album.apple_music_url,
        'youtube_url': album.youtube_url,
        'release_date': release_date,
    }
    return JsonResponse(data)

