from django.conf.urls import url
from ratemy import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'faq/$', views.faq, name='faq'),
    url(r'home/$', views.home, name='home'),
    url(r'contact_us/$', views.contact_us, name='contact_us'),
]