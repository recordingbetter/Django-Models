from django.conf.urls import url

from . import views

app_name = 'bbs'
urlpatterns = [
    url(r'^$', views.article_list, name = 'list'),
    url(r'^(?P<pk>\d+)/$', views.article_detail, name = 'article_detail')
]