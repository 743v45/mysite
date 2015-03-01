from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$','index'),
    url(r'^page/(\d+)/$','index'),
    url(r'^blog/(\d+)/$','blog'),
    url(r'^tag/(?P<id>\d+)/$','tag'),
    url(r'^tag/(?P<id>\d+)/(?P<page_num>\d+)/$','tag'),

)
