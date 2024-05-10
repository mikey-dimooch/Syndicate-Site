from django.shortcuts import render, redirect
from .models import Show
from django.utils import timezone
from django.core.mail import send_mail

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

