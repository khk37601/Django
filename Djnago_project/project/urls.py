from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url,include

from .views import RestAPI

routers = routers.DefaultRouter()
routers.register('premier',RestAPI)

urlpatterns = [
    #path('', views.main, name='main'),
    path('', views.main, name="/"),
    path('sign', views.sign, name='sign'),
    path('post_sign', views.post_sign, name='post_sign'),
    path('signup', views.signup, name='signup'),
    path('post_signup',views.post_signup, name='post_signup'),
    path('logout', views.logout, name='logout'),
    path('check_email', views.check_email, name='check_email'),
    path('start_scheduler', views.start_scheduler, name='start_scheduler'),
    path('shutdown', views.shutdown, name='shutdown'),
    path('email_duplicate_check', views.email_duplicate_check, name='email_duplicate_check'),
    url(r'^', include(routers.urls)),

]