from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)', DetailView.as_view(model=Post, template_name='blog/post.html')),
               url(r'^create/$', views.post_create, name='create'),
               url(r'^delete/$', views.post_delete, name='delete'),
               url(r'^(?P<pk>\d+)/edit$', views.post_update, name='update'),
               url(r'^detail/$', views.post_detail, name='detail'),
               url(r'^list/$', views.post_list, name='list'),
            



               ]
