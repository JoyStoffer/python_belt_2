from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^wishes$', views.wishes, name = "dashboard"),
    url(r'^add$', views.add, name = "add_wish"),
    url(r'^delete_wish/(?P<id>\d+)$', views.delete_wish, name = "delete_wish"),
    url(r'^create$', views.create, name = "create_wish"),
    url(r'^wish_item/(?P<id>\d+)$', views.add_wish_item, name = "add_wish_item"),
    url(r'^remove_wish_item/(?P<id>\d+)$', views.remove_wish_item, name = "remove_wish_item"),
    url(r'^wish_item/(?P<id>\d+)$', views.wish_item, name = "wish_item"),

]
