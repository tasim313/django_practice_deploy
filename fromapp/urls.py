from django.urls import path

from . import customer_views, music_view

app_name = 'customer'

urlpatterns = [
    path('home', customer_views.customer_home, name='home'),
    path('index', customer_views.index, name='index'),
    path('main/', music_view.index, name='home'),
    path('album', music_view.album_form, name='album'),
    path('album_list/<int:artist_id>/', music_view.album_list, name='album_list'),
    path('musician', music_view.musician_form, name='musician'),
    path('edit_artist/<int:artist_id>/', music_view.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', music_view.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', music_view.delete_album, name='delete_album'),
    path('delete_musician/<int:artist_id>/', music_view.delete_musician, name='delete_musician'),
]