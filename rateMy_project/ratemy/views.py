from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse("This will be the Home page <br/> <a href='/ratemy/about/'>About</a>")



def about(request):
    return HttpResponse("This will be the about page <br/> <a href='/ratemy/'>Home</a> ")