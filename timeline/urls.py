from django.conf.urls import url
from django.contrib import admin

from .views import (
	media_list,
	media_create,
	media_detail,
	media_update,
	media_delete,
	)

urlpatterns = [
    url(r'^$', media_list, name='list'),
    url(r'^create/$', media_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', media_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', media_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', media_delete, name='delete'),
]