from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('playlists/', views.playlists_index, name='index'),
    path('playlists/<int:playlist_id>/', views.playlists_detail, name='detail'),
    path('playlists/create/', views.PlaylistCreate.as_view(),
         name='playlists_create'),
    path('playlists/<int:pk>/update',
         views.PlaylistUpdate.as_view(), name='playlists_update'),
    path('playlists/<int:pk>/delete',
         views.PlaylistDelete.as_view(), name='playlists_delete'),
]
