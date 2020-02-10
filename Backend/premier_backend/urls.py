from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static


#routers = routers.DefaultRouter()
#routers.register('premier_league', RestTest)

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$',views.premier_league_list.as_view(),name='premier_league_list'),
    url(r'^premier_league_list/(?P<team_name>[-\w]+)/delete$', views.PremierLeague_Delete.as_view(), name="delete"),
    url(r'^premier_league_list/(?P<team_name>[-\w]+)/update$', views.PremierLeague_update.as_view(), name="update"),
    url(r'^premier_league_list/(?P<team_name>[-\w]+)/$', views.premier_league_detail_list.as_view(), name="detail"),
    #url(r'^',include(routers.urls))
    url(r'^premier_league_list/$', views.premier_league_list.as_view(), name="premier_league_list"),


]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
