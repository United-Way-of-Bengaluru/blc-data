from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

from schools.views import HomeView

urlpatterns = patterns('',
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', RedirectView.as_view(url='/site')),
    #url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),

    #url(r'^api/', include('dise_dashboard.api_urls')),

    url(r'^site/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^explorer/', include('explorer.urls')),
)
