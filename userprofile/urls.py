from django.conf.urls import patterns, include, url


urlpatterns = patterns('userprofile.views',
    #(r'^(?P<pk>\d+)/$', 'view_profile'),
    (r'^$', 'view_profile'),
    

)
