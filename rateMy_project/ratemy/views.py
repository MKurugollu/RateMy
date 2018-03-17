from django.shortcuts import render
from django.http import HttpResponse
from ratemy.models import Category, Post


def landing(request):
    category_list = Category.objects.order_by('-followers')[:5]
    post_list = Post.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list, 'posts': post_list}

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
    post_list = Post.objects.order_by('-likes')[:20]

    context_dict = {'posts': post_list}
    return render(request, 'ratemy/home.html', context_dict)


def add_category(request):
    context_dict = {}
    return render(request, 'ratemy/add_category.html', context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except:
        context_dict['posts'] = None
        context_dict['category'] = None

    return render(request, 'ratemy/category.html', context_dict)


def show_post(request, post_title_slug, category_name_slug):
    context_dict = {}
    try:
        post = Post.objects.get(slug=post_title_slug)
        context_dict['post'] = post
    except:
        context_dict['post'] = None
    return render(request, 'ratemy/post.html', context_dict)
