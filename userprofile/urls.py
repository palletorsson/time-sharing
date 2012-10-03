from django.conf.urls import patterns, include, url


urlpatterns = patterns('userprofile.views',
    url(r'^$', 'view_profile'),
    url(r'^edit/(?P<id>\d+)/$', 'edit', name='edit_profile'),
)