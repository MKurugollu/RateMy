from django import forms
from django.utils import timezone
from ratemy.models import Post, Category, UserProfile
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image=forms.ImageField()
    followers = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Category
        fields = ('name','image')


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    category = forms.CharField(widget=forms.HiddenInput(), initial = 0)
    picture = forms.ImageField()
    created_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())

    class Meta:
        model = Post
        fields = ('title', 'picture')

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    picture = forms.ImageField(required = True)

    bio = forms.CharField(required=False)

    age = forms.IntegerField(required=True)

    fb = forms.URLField(required=False)
    instagram = forms.URLField(required=False)
    twitter = forms.URLField(required=False)

    country = LazyTypedChoiceField(choices=countries)

    class Meta:
        model = UserProfile
        exclude = ('user', )
