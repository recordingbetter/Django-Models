from django.conf.urls import url

from . import views

app_name = 'bbs'
urlpatterns = [
    url(r'^$', views.article_list, name = 'list'),
    url(r'^(?P<pk>\d+)/$', views.article_detail, name = 'article_detail'),
    url(r'^add/$', views.article_add, name = 'article_add'),
    url(r'^markdown/$', views.article_markdown, name = 'markdown'),
    url(r'^(?P<pk>\d+)/modify/$', views.article_modify, name = "article_modify"),
    url(r'^(?P<pk>\d+)/delete/$', views.article_delete, name = 'article_delete'),

]