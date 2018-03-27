from django.conf.urls import url
from ratemy import views, views_ajax

urlpatterns = [
    url(r'about/$', views.about, name='about'),
    url(r'register_profile/$', views.register_profile, name='register_profile'),
    url('faq/$', views.faq, name='faq'),
    url(r'home/$', views.home, name='home'),
    url(r'contact_us/$', views.contact_us, name='contact_us'),
    url(r'add_cat/$', views.add_category, name='add_category'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/add_post/$',
        views.add_post, name='add_post'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/((?P<post_title_slug>[\w\-]+))/$',
        views.show_post, name='show_post'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', # the regular expression [\w\-]+ will look for any sequence of alphanumeric characters (denoted by the \w, and any hyphens (denoted by the \- and we can match as many as we like (denoted by the []+ expression)
        views.show_category, name='show_category'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),

    url(r'catagory_list/$', views.catagory_list, name='catagory_list'),
    url(r'follow_category/$', views_ajax.follow_category, name='follow_category'),
    url(r'like_post/$', views_ajax.like_post, name='like_post'),


]
