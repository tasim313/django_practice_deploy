from django.shortcuts import render
from . import musician_forms, album_forms
from . import music_models
from django.db.models import Avg


def index(request):
    musician_list = music_models.musicians.objects.order_by('first_name')
    diction = {'title': 'Home Page', 'musician_list': musician_list}
    return render(request, 'music/index.html', context=diction)


def album_list(request, artist_id):
    artist_info = music_models.musicians.objects.get(pk=artist_id)
    album_list = music_models.album.objects.filter(artist=artist_id).order_by('num_star')
    artist_rating = music_models.album.objects.filter(artist=artist_id).aggregate(Avg('num_star'))
    diction = {'title': 'List of Album', 'artist_info': artist_info, 'album_list': album_list, 'artist_rating': artist_rating}
    return render(request, 'music/album_list.html', context=diction)


def musician_form(request):
    form = musician_forms.musician_form()
    if request.method == 'POST':
        form = musician_forms.musician_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': 'Add Musician', 'form': form}
    return render(request, 'music/musician_form.html', context=diction)


def album_form(request):
    form = album_forms.album_form()
    if request.method == 'POST':
        form = album_forms.album_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title': "Add Album", 'form': form}
    return render(request, 'music/album_form.html', context=diction)


def edit_artist(request, artist_id):
    artist_info = music_models.musicians.objects.get(pk=artist_id)
    form = musician_forms.musician_form(instance=artist_info)
    if request.method == 'POST':
        form = musician_forms.musician_form(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    diction = {"form": form, 'title': 'Edit Information'}
    return render(request, 'music/edit_artist.html', context=diction)


def edit_album(request, album_id):
    album_info = music_models.album.objects.get(pk=album_id)
    form = album_forms.album_form(instance=album_info)

    if request.method == 'POST':
        form = album_forms.album_form(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, album_id)
    diction = {'form': form}
    diction.update({'album_id': album_id})
    return render(request, 'music/edit_album.html', context=diction)


def delete_album(request, album_id):
    album = music_models.album.objects.get(pk=album_id).delete()
    diction = {'deleted_success': 'Album Delete Successfully'}
    return render(request, 'music/delete.html', diction)


def delete_musician(request, artist_id):
    musician = music_models.musicians.objects.get(pk=artist_id).delete(0)
    diction = {'deleted_success': 'Musician Delete Successfully'}
    return render(request, 'music/delete.html', context=diction)
