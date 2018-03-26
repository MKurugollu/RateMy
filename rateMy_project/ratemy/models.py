from django.db import models
from django.utils import timezone # For Created Time
from django.template.defaultfilters import slugify #  Used to slugify the urls
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=18, unique=True) # name of the category

    image = models.ImageField(upload_to='category_images') # image upload
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(unique=True)
    followers = models.IntegerField(default=0)# num of authorised users following/liking(?) the category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category = models.ForeignKey(Category) # cat the post is in
    title = models.CharField(max_length=26) # title of post
    #description = models.CharField(max_length=300, blank = True) # description of post
    picture = models.ImageField(upload_to='post_images') # image upload
    likes = models.IntegerField(default=0) # num of likes
    created_date = models.DateTimeField(default=timezone.now) # date the post is created this is for ordering the posts

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # These will be the links to the social media of the User

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    age = models.IntegerField(default=0)

    country = CountryField(blank=False)

    fb = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    picture = models.ImageField(upload_to='profile_images', blank=False)

    bio = models.CharField(max_length=250)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
