from django.shortcuts import render, HttpResponse
from .models import Musician
# Create your views here.
def index(request):
    for m in Musician.objects.all():
        print(m.name)
    return HttpResponse("Hello this is tannersapp")

def another_method(request, table):
    return HttpResponse("This is another method, with table: " + table)