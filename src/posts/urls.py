from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    # url(r'^$', views.post_home),
    url(r'^$', 'posts.views.post_list'),
    url(r'^detail/$', 'posts.views.post_detail'),
    url(r'^create/$', 'posts.views.post_create'),
    url(r'^delete/$', 'posts.views.post_delete'),
    url(r'^update/$', 'posts.views.post_update'),

]
