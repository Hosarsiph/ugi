# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

js_info_dict = {
    'packages': ('ugi.mia',),
}

urlpatterns = patterns('',
                        url(r'^mia_list/$', 'ugi.mia.views.mia_list', name='mia_list'),
                        url(r'^mia_new/$', 'ugi.mia.views.mia_new', name='mia_new'),
                        url(r'^mia_detail/(?P<pk>[0-9]+)/$', 'ugi.mia.views.mia_detail', name='mia_detail'),
                        url(r'^mia_detail/(?P<pk>[0-9]+)/edit/$', 'ugi.mia.views.mia_edit', name='mia_edit'),
                        )
