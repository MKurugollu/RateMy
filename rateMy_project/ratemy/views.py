from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {}
    return render(request, 'ratemy/home.html', context=context_dict) #second param is for the Directory of the hmtl template



def about(request):
    return HttpResponse("This will be the about page <br/> <a href='/ratemy/'>Home</a> ")