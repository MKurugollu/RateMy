from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    context_dict = {}
    return render(request, 'ratemy/landing.html', context=context_dict) #second param is for the Directory of the hmtl template


def about(request):
    context_dict = {}
    return render(request, 'ratemy/about.html', context=context_dict)


def faq(request):
    context_dict = {}
    return render(request, 'ratemy/faq.html', context=context_dict)


def contact_us(request):
    context_dict = {}
    return render(request, 'ratemy/contact_us.html', context_dict)


def home(request):
    context_dict = {}
    return render(request, 'ratemy/home.html', context_dict)