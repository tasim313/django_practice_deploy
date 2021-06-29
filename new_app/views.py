from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
import fromapp.models
from .models import musicians, album
from fromapp import music_models


# Create your views here.


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello World!!")


class HomeView(TemplateView):
    template_name = 'new_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Breaking_News'] = 'Today start Lockdown....Everyone Should Stay At Home'
        context['Sports_News'] = 'Bangladesh will be played India in Two Test match '
        return context


class MusicianView(ListView):
    context_object_name = 'musicians_list'
    model = musicians
    template_name = 'new_app/musician_view.html'


class AlbumView(ListView):
    context_object_name = 'album_list'
    model = fromapp.music_models.album
    template_name = 'new_app/album.html'


class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = musicians
    template_name = 'new_app/musicianDetails.html'


class MusicianCreate(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = musicians
    template_name = 'new_app/add_musician.html'


class MusicianUpdate(UpdateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = musicians
    template_name = 'new_app/add_musician.html'


class MusicianDelete(DeleteView):
    context_object_name = 'musician'
    model = musicians
    success_url = reverse_lazy('first:musician_view')
    template_name = 'new_app/delete_musician.html'