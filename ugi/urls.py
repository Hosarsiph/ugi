# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin


# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'ugi.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# ]
js_info_dict = {
    'domain': 'djangojs',
    'packages': ('ugi',)
}

urlpatterns = patterns('',

                        # Static pages
                        # url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),
                        url(r'^$', 'ugi.people.views.login_people', name='login_people'),
                        url(r'^admin/', include(admin.site.urls)),

                         # Mia views
                         (r'^/', include('ugi.mia.urls')),

                         # People views
                         (r'^', include('ugi.people.urls')),
                         # url(r'^profile_detail/$','ugi.people.views.profile_detail'),


                        )
