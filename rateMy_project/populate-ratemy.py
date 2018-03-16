import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rateMy_project.settings')

import django

django.setup()

from ratemy.models import Category, Post


def populate():
    barber_posts = [
        {"title": "Bad Barber",
         "picture": "post_images/barber-2.jpeg",
         "likes": 300},
        {"title": "Good Barber",
         "picture": "post_images/barber-1.jpeg",
         "likes": 69},
        {"title": "West Glasgow Barber",
         "picture": "post_images/barber-3.jpg",
         "likes": 10}
    ]
    
    faceswap_posts = [
        {"title": "Good faceswap",
         "picture": "post_images/faceswap-1.jpg",
         "likes": 250},
        {"title": "Bad faceswap",
         "picture": "post_images/faceswap-2.jpg",
         "likes": 25},
        {"title": "Hilarious faceswap",
         "picture": "post_images/faceswap-3.jpg",
         "likes": 532}
    ]
    
    cats = {"Barber": {"posts": barber_posts, "followers": 450},
            "FaceSwap": {"posts": faceswap_posts, "followers": 300}
            }
    # if you want to add more catergories or pages, add them to the dictionaries above

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_items_to_iterate_over_a_dictionary.html
    # for more information about using items() and how to iterate over a dictionary properly

    # Using the .items returns the key and the value. In this case the key is "Python", "Django" or "Other Frameworks" and the value (cat_data) is the corresponding dictionary in cats.


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["followers"])
        for p in cat_data["posts"]:
            add_post(c, p["title"], p["picture"], p["likes"])

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Post.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))




def add_post(cat, title, picture, likes):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    # we need to save the changes we made!!
    p.picture = picture
    p.likes = likes
    p.save()
    return p


def add_cat(name, followers):
    c = Category.objects.get_or_create(name=name)[0]
    c.followers = followers
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting RateMy population script...")
    populate()