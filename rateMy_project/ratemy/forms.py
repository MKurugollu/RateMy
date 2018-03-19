from django import forms
from django.utils import timezone
from ratemy.models import Post, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    category = forms.CharField(widget=forms.HiddenInput(), initial = 0)
    picture = forms.ImageField()
    created_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())

    class Meta:
        model = Post
        fields = ('title', 'picture')