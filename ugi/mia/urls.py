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
                        url(r'^mia/$', 'ugi.mia.views.mia_list', name='mia_list'),
                        url(r'^mia/(?P<pk>[0-9]+)/$', 'ugi.mia.views.mia_detail', name='mia_detail'),
                        url(r'^mia/(?P<pk>[0-9]+)/edit/$', 'ugi.mia.views.mia_edit', name='mia_edit'),
                        url(r'^mia_new/$', 'ugi.mia.views.mia_new', name='mia_new'),
                        url(r'^filter/$', 'ugi.mia.views.filter_mia', name='filter_mia'), # filter_date
                        url(r'^filter_date/$', 'ugi.mia.views.filter_date', name='filter_date'),
                        )
