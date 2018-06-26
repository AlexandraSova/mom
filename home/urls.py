from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^about/$', views.about, name='about'),
url(r'^rewards/$', views.rewards, name='rewards'),
url(r'^news/$', views.news, name='news'),
]