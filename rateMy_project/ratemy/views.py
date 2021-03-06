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
from datetime import datetime

def landing(request):

    category_list = Category.objects.order_by('-followers')[:5]
    post_list = Post.objects.order_by('-likes')[:5]
    visits = int(request.COOKIES.get('visits', '1'))
    context_dict = {'categories': category_list, 'posts': post_list, 'visits': visits}

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'ratemy/landing.html', context=context_dict) #second param is for the Directory of the hmtl template
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request, response)
    # Return response back to the user, updating any cookies that need changed.
    return response


def about(request):
    context_dict = {}
    return render(request, 'ratemy/about.html', context=context_dict)


def faq(request):
    context_dict = {}
    return render(request, 'ratemy/faq.html', context=context_dict)


def contact_us(request):
    context_dict = {}
    return render(request, 'ratemy/contact_us.html', context_dict)

@page_template('myapp/home.html')
def home(request, template = 'ratemy/home.html', extra_context=None):

    context_dict = {'posts': Post.objects.order_by('-likes'),}
    if extra_context is not None:
        context_dict.update(extra_context)
    return render(request, template, context_dict)

def visitor_cookie_handler(request, response):
    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, then the default value of 1 is used.
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).seconds > 60:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        # Set the last visit cookie
        response.set_cookie('last_visit', last_visit_cookie)
    # Update/set the visits cookie
    response.set_cookie('visits', visits)


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
    query=request.GET.get('search')
    sort=request.GET.get('sort')

    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)

        if sort:
            if sort=='likes':
                sort='-likes'
            posts=posts.order_by(sort)
            context_dict['posts'] = posts
            context_dict['category'] = category

        elif query:
            print(query)
            posts= Post.objects.filter(category=category) & Post.objects.filter(Q(title__icontains=query))
            context_dict['posts'] = posts
            context_dict['category'] = category
        else:
            posts= Post.objects.filter(category=category)
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
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'ratemy/profile_registration.html', context_dict)


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    userprofile = UserProfile.objects.filter(user=user)[0]
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
        # return HttpResponseRedirect(reverse('Home'))
    else:
        print(form.errors)
    return render(request, 'ratemy/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form, 'posts': posts})


def list_profiles(request):

    userprofile_list=UserProfile.objects.all()
    query=request.GET.get('search')
    sort=request.GET.get('sort')

    if sort:
        if sort=='first name':
            sort='first_name'
        userprofile_list=UserProfile.objects.order_by(sort)

    if query:

        userprofile_list= UserProfile.objects.filter( Q(user__username__icontains=query) )


    context_dict = {'userprofile_list': userprofile_list}




    return render(request, 'ratemy/list_profiles.html', context_dict)



def catagory_list(request):
    category_list = Category.objects.all()



    sort=request.GET.get('sort')
    query=request.GET.get('search')



    if sort:
        if sort=='followers':
            sort="-followers"
        print(sort)
        category_list=Category.objects.order_by(sort)


    if query:

        category_list= Category.objects.filter(Q(name__icontains=query) | Q(author__username__icontains=query) )


    context_dict = {'categories': category_list}

    return render(request, 'ratemy/catagory_list.html', context=context_dict)


