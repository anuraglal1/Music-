from django.conf.urls import url,include
from . import views

app_name='music'

urlpatterns = [
	# /music/

    url(r'^$',views.IndexView.as_view(), name='index' ),

    url(r'^register/$',views.UserFormView.as_view(), name='register' ),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    
    #/muisc/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(),name='album-add'),
    #/muisc/album/2/
	url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name='album-update'),

	#/muisc/album/2/delete/
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name='album-delete'),
  


  ]

