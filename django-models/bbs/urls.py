from django.conf.urls import url

from . import views

app_name = 'bbs'
urlpatterns = [
    url(r'^$', views.article_list, name = 'list'),
]