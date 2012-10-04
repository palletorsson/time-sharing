from django.conf.urls import patterns, include, url


urlpatterns = patterns('userprofile.views',
    url(r'^$', 'view_profile', name='view_profile'),
    url(r'^edit/$', 'edit', name='edit_profile'),
)