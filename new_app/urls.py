from django.urls import path
from .views import IndexView, HomeView, MusicianView, AlbumView, MusicianDetails, MusicianCreate, MusicianUpdate, MusicianDelete
from . import views
app_name = 'first'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('musician/', views.MusicianView.as_view(), name='musician_view'),
    path('album/', views.AlbumView.as_view(), name='album'),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name='musician_details'),
    path('add_musician/', views.MusicianCreate.as_view(), name='add_musician'),
    path('update_musician/<pk>/', views.MusicianUpdate.as_view(), name='update_musician'),
    path('delete_musician/<pk>/', views.MusicianDelete.as_view(), name='delete_musician'),
]