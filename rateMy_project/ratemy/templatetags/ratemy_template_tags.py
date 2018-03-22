from django import template
from ratemy.models import Category, UserProfile
from django.contrib.auth.models import User

register = template.Library()

# @register.inclusion_tag('rango/cats.html')
# def get_category_list(cat=None):
#     return {'cats': Category.objects.all(), 'act_cat': cat}

@register.inclusion_tag('ratemy/get_profile_pic.html')
def find_userprofile(cat = None):

    return {'userprofiles': UserProfile.objects.all(), 'act_act': cat}