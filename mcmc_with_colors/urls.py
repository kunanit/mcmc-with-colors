from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'mcmc_with_colors.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^colortask/', include('colortask.urls', namespace='colortask')),
    
)
