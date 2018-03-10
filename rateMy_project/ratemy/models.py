from django.db import models
from django.utils import timezone # For Created Time
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=18, unique=True) # name of the category
    followers = models.IntegerField(default=0) # num of authorised users following/liking(?) the category

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category) # cat the post is in
    title = models.CharField(max_length=128) # title of post
    desc = models.CharField(max_length=300) # description of post
    views = models.IntegerField(default=0) # num of views (may not be necessary)
    likes = models.IntegerField(default=0) # num of likes
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # the authorised user that created the post
    created_date = models.DateTimeField(default=timezone.now) # date the post is created this is for ordering the posts

    def __str__(self):
        return self.title