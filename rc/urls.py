from django.conf.urls import patterns, include, url
from rc import views

urlpatterns = patterns(
    '',
    url(r'^$', views.all_rc, name='all_rc'),
    url(r'^(?P<id>\d+)/$', views.rc, name='rc'),
)

