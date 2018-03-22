import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rateMy_project.settings')

import django
django.setup()
from django.contrib.auth.models import User

django.setup()

from ratemy.models import Category, Post


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
         "likes": 250000,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
         {"title": "Blastoise",
         "picture": "post_images_pop/Blastoise.jpg",
         "likes": 100000,
         "author": User.objects.get(username='admin'),
         "date": timezone.now},
         {"title": "Gengar",
         "picture": "post_images_pop/Gengar.jpg",
         "likes": 200000,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}

    ]

    why_tho_posts=[{"title": "Rate my?",
         "picture": "post_images_pop/Ratemy.PNG",
         "likes": 0,
         "author": User.objects.get(username='admin'),
         "date": timezone.now}

    ]
    
    cats = {"Barber": {"posts": barber_posts, "followers": 450, "image": "category_images/pokemon.PNG"},
            "Face Swap": {"posts": faceswap_posts, "followers": 300,"image": "category_images/pokemon.PNG"},
            "Pokemon": {"posts": pokemon_posts, "followers":1000000, "image":"category_images/pokemon.PNG"},
            "Why tho": {"posts": why_tho_posts, "followers":1,"image":"category_images/pokemon.PNG"}
            }

    # if you want to add more catergories or pages, add them to the dictionaries above

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_items_to_iterate_over_a_dictionary.html
    # for more information about using items() and how to iterate over a dictionary properly

    # Using the .items returns the key and the value. In this case the key is "Python", "Django" or "Other Frameworks" and the value (cat_data) is the corresponding dictionary in cats.


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["followers"], cat_data["image"])
        for p in cat_data["posts"]:
            add_post(c, p["title"], p["picture"], p["likes"], p["date"], p["author"])  #

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))




def add_post(cat, title, picture, likes, date, author) :# author,
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.picture = picture
    p.likes = likes
    p.author = author
    p.date = date
    p.save()
    return p


def add_cat(name, followers,image):
    c = Category.objects.get_or_create(name=name)[0]
    c.followers = followers
    c.image = image
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting RateMy population script...")
    populate()
