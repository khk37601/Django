from django.urls import path
from . import views
from django.conf.urls import url,include
from django.conf.urls import (handler404, handler400, handler500)


urlpatterns = [
    path('', views.index, name="/"),
    url(r'^Search$', views.Search.as_view(), name="Search"),
    url(r'^login$', views.PostLogin.as_view(), name="login"),
    url(r'^logout$', views.logout, name="logout"),
]

#handler404 = 'premier_front.views.page_not_found'
