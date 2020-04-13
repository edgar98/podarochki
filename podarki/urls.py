from django.conf.urls import url

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^list/$', views.ShopListView.as_view(), name='list'),
    url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='detail'),
]
