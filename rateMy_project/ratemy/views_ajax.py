from django.shortcuts import render
from django.http import HttpResponse
from ratemy.models import Category, Post, UserProfile
from ratemy.forms import CategoryForm, PostForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from el_pagination.decorators import page_template
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

@login_required
def follow_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
    followers = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            followers = cat.followers + 1
            cat.followers = followers
            cat.save()
    return HttpResponse(followers)

@login_required
def like_post(request):
    post_id = None
    button_id=None


    if request.method == 'GET':

        post_id = request.GET['post_id']
        button_id= request.GET.get('button_id')

    likes = 0

    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            if button_id=='like':
                likes = post.likes + 1
                post.likes = likes
                post.save()
            elif button_id=='unlike':
                likes = post.likes - 1
                post.likes = likes
                post.save()

    return HttpResponse(likes)

