# from django.shortcuts import render
from django.http import HttpResponse  # new


# Create your views here.
def home_page_view(request):
    return HttpResponse("¡Hola mundo!")