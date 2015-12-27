from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coins_list/', views.coins_list, name='coins_list'),
    url(r'^coin/(?P<pk>[0-9]+)/$', views.coin_detail, name='coin_detail'),
    url(r'^coin/new/$', views.coin_new, name='coin_new'),
    url(r'^coin/(?P<pk>[0-9]+)/remove/$', views.coin_remove, name='coin_remove'),
    url(r'^coin/(?P<pk>[0-9]+)/edit/$', views.coin_edit, name='coin_edit'),
]