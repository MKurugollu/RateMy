from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ratemy.models import Category, Post, UserProfile
from ratemy.forms import CategoryForm, PostForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'ratemy/add_category.html', {'form': form})


@login_required
def add_post(request, category_name_slug):
    category = Category.objects.get(slug = category_name_slug)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if category:
                post = form.save(commit=False)
                post.category = category
                post.author = request.user
                post.likes = 0
                post.save()
                return show_category(request, category_name_slug)

        else:
            print(form.errors)
    context_dict = {'form':form, 'category': category}
    return render(request, 'ratemy/add_post.html', context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        posts = posts.order_by('-likes')
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

@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'ratemy/profile_registration.html', context_dict)

def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form =UserProfileForm(
        {'picture': userprofile.picture, 'bio':userprofile.bio, 'age':userprofile.age, 'country':userprofile.country,
         'first_name':userprofile.first_name, 'last_name':userprofile.last_name, 'fb':userprofile.fb,
         'instagram':userprofile.instagram, 'twitter':userprofile.twitter}
    )

    posts = Post.objects.filter(author = user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profile', user.username)
    else:
        print(form.errors)
    return render(request, 'ratemy/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form, 'posts': posts})


def list_profiles(request):
    userprofile_list = UserProfile.objects.all()

    return render(request, 'ratemy/list_profiles.html', {'userprofile_list': userprofile_list})


