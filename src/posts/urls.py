from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update,
)


urlpatterns = [
    # url(r'^$', views.post_home),
    url(r'^$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail,name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update,name= 'update'),
    url(r'^create/$', post_create),
    url(r'^delete/$', post_delete),
    url(r'^update/$', post_update),

]
