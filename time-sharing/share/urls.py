from django.views.generic import ListView
from django.conf.urls import patterns, include, url
from models import Share

urlpatterns = patterns('share.views',
    url(r'^$', ListView.as_view(
            queryset = Share.objects.all().order_by('-created')[:10],
            template_name = 'share/index.html',  
            context_object_name = 'ads',
        ),
        name = 'list_ads',
    ),  
    url(r'^(?P<pk>\d+)/$', 'detail', name= 'detail_page'),
    url(r'^add/$', 'add_ad', name='add_ad'),
    url(r'^delete/(?P<pk>\d+)/$', 'delete_ad', name='delete_ad'),
    url(r'^edit/(?P<pk>\d+)/$', 'edit_ad', name='edit_ad'),
)