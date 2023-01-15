from django.shortcuts import render
from .models import ClubMember
from .models import Movie


def home(request):
    mems = ClubMember.objects.all
    return render(request, 'home.html', {'dets': mems})

def login(request):
    mems = ClubMember.objects.all
    return render(request, 'login.html', {'dets': mems})

def booking(request):
    movie_list = Movie.objects.all
    return render(request, 'booking.html', {'movie_list': movie_list})

