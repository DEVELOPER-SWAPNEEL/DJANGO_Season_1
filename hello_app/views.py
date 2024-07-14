from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("HELLO NIKU!!<br><br>WELCOME TO MY FIRST DJANGO WEBSITE!")

# Create your views here.
