from django.conf.urls import patterns, include, url


urlpatterns = patterns('share.views',
    (r'^$', 'ads'),
    (r'^(?P<pk>\d+)/$', 'detail'),
    (r'^add/$', 'add_ad'),

)
