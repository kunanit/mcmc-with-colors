from django.conf.urls import patterns, url

from colortask import views


urlpatterns = patterns('',
	url(r'^instructions/$',views.instructions, name='instructions'),
    # url(r'^dataviewer/(?P<pk>\d+)/$', views.dataviewer, name='dataviewer'),
    url(r'^stage/$',views.stage, name='stage'),
    url(r'^conclusion/$',views.conclusion, name='conclusion'),

    url(r'^initialize/$',views.initialize, name='initialize'),
    url(r'^proposal/$',views.proposal, name='proposal'),
    url(r'^save/$',views.save, name='save'),
)