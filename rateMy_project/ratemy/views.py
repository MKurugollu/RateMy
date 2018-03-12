from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ratemy.webhose_search import run_query

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

def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
             # Run our Webhose function to get the results list!
             result_list = run_query(query)
    return render(request, 'ratemy/search.html', {'result_list': result_list})