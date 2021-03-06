import os
from django.utils import timezone
from django_countries.fields import CountryField
from django_countries import countries
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rateMy_project.settings')

import django
django.setup()
from django.contrib.auth.models import User


django.setup()

from ratemy.models import Category, Post, UserProfile


def populate():

    barber_posts = [
        {"title": "Bad Barber",
         "picture": "post_images_pop/barber-2.jpeg",
         "likes": 10,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
        {"title": "Good Barber",
         "picture": "post_images_pop/barber-1.jpeg",
         "likes": 69,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
        {"title": "West Glasgow Barber",
         "picture": "post_images_pop/barber-3.jpg",
         "likes": 300,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}
    ]

    faceswap_posts = [
        {"title": "Good faceswap",
         "picture": "post_images_pop/faceswap-1.jpg",
         "likes": 250,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
        {"title": "Bad faceswap",
         "picture": "post_images_pop/faceswap-2.jpg",
         "likes": 25,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
        {"title": "Hilarious faceswap",
         "picture": "post_images_pop/faceswap-3.jpg",
         "likes": 532,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}
    ]

    pokemon_posts=[{"title": "Charizard",
         "picture": "post_images_pop/charizard.jpg",
         "likes": 250,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
         {"title": "Blastoise",
         "picture": "post_images_pop/Blastoise.jpg",
         "likes": 100,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
         {"title": "Gengar",
         "picture": "post_images_pop/Gengar.jpg",
         "likes": 200,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}

    ]

    why_tho_posts=[{"title": "Rate my?",
         "picture": "post_images_pop/Ratemy.PNG",
         "likes": 0,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}

    ]

    weird_dogs=[
        {"title": "What even is doge?",
         "picture": "post_images_pop/weird_doge.jpg",
         "likes": 78,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},

        {"title": "Janitor dog",
         "picture": "post_images_pop/mop_dog.jpg",
         "likes": 498,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},

        {"title": "Happy dog",
         "picture": "post_images_pop/happy_dog.jpg",
         "likes": 338,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},

        {"title": "Nice Doge",
         "picture": "post_images_pop/doge.jpg",
         "likes": 128,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}


    ]



    cats = {"Barber": {"posts": barber_posts, "followers": 450,
                       "image": "category_images/Barber_sign.jpg",
                       "author": User.objects.get(username='admin')},

            "Face Swap": {"posts": faceswap_posts, "followers": 300,
                          "image": "category_images/bean-mona.jpg",
                          "author": User.objects.get(username='admin')},

            "Pokemon": {"posts": pokemon_posts, "followers":100,
                        "image":"category_images/pokemon.png",
                        "author": User.objects.get(username='admin')},

            "Why tho": {"posts": why_tho_posts, "followers":1,
                        "image":"category_images/why_tho.jpg",
                        "author": User.objects.get(username='admin')},

            "Weird Dogs": {"posts": weird_dogs, "followers":560,
                        "image":"category_images/Nice.jpg",
                        "author": User.objects.get(username='admin')}
            }

    #PLEASE NOTE: A User Profile requires a User model. When website is first launched on your local machine the only user model is
    #the admin user. Therefore we could not populate the User Profiles other than for the admin user. If you would like to see a
    #populated version please look at the "profiles" tab on the pythonanywhere website. We added a few usermodels manually.
    # Or you could manually add a register a few User models and add their info for their User Profile.  Thank you.

    admin_info = [{"username": User.objects.get(username = "admin"),
                    "first_name": "Mustafa",
                   "last_name": "Kurugollu",
                   "age":20,
                   "country":"TR",
                   "fb": "https//:www.facebook.com",
                   "instagram":"https://www.instagram.com/",
                   "twitter":"https://twitter.com/",
                   "picture":"profile_images/admin.png",
                   "bio":"I don't like Pokemon"}
    ]

    users= {"user1":{"info": admin_info}

    }

    # if you want to add more catergories or pages, add them to the dictionaries above

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_items_to_iterate_over_a_dictionary.html
    # for more information about using items() and how to iterate over a dictionary properly


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["followers"], cat_data["image"], cat_data["author"])
        for p in cat_data["posts"]:
            add_post(c, p["title"], p["picture"], p["likes"], p["date"], p["author"])

    for user_p, user_data in users.items():

        for i in user_data["info"]:
            add_user(i["username"], i["first_name"], i["last_name"], i["age"], i["country"], i["fb"], i["instagram"],
                     i["twitter"], i["picture"], i["bio"])
    # Print out what we have added to the user.

    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))



    for u in UserProfile.objects.all():
         print("- {0} -".format(str(u)))


def add_post(cat, title, picture, likes, date, author) :
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.picture = picture
    p.likes = likes
    p.author = author
    p.date = date
    p.save()
    return p


def add_cat(name, followers,image, author):
    c = Category.objects.get_or_create(name=name)[0]
    c.followers = followers
    c.image = image
    c.author = author
    c.save()
    return c


def add_user(username, first_name, last_name, age, country, fb, instagram, twitter, picture, bio):
    u = UserProfile.objects.get_or_create(user=username)[0]
    u.first_name = first_name
    u.last_name=last_name
    u.age = age
    u.country = country
    u.fb = fb
    u.instagram = instagram
    u.twitter = twitter
    u.picture = picture
    u.bio = bio
    u.save()
    return u


# Start execution here!
if __name__ == '__main__':
    print("Starting RateMy population script...")
    populate()
