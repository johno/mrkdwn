from django.conf.urls import patterns, url

from notepad import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<note_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<note_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<note_id>\d+)/update/$', views.update, name='update'),
)
