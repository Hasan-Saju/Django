from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
from django.db.models import Avg, Max, Min


# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title': "Home Page", 'musician_list': musician_list}
    return render(request, 'first_app/index.htm', context=diction)


def album_list(request, artist_id):

    artist_info = Musician.objects.get(pk=artist_id)
    # pk diye search er jonno get
    album_list = Album.objects.filter(
        artist=artist_id).order_by('name', 'release_date')
    # pk na hole filter
    artist_rating = Album.objects.filter(
        artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title': "List of Album",
               'artist_info': artist_info, 'album_list': album_list, 'artist_rating': artist_rating}
    return render(request, 'first_app/album_list.htm', context=diction)


def musician_form(request):
    form = forms.MusicianForm()

    # action for submit button
    if request.method == 'POST':
        # info gula shob form a overwrite
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': "Add Musician", 'musician_form': form}
    return render(request, 'first_app/musician_form.htm', context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': "Add Album", 'album_form': form}
    return render(request, 'first_app/album_form.htm', context=diction)


def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    # instance value gula load kore
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        # ager value , porer shob gula ana lage
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)

    diction = {'edit_form': form}
    return render(request, 'first_app/edit_artist.htm', context=diction)


def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text': 'Successfully Updated'})

    diction.update({'edit_form': form})
    diction.update({'album_id': album_id})
    return render(request, 'first_app/edit_album.htm', context=diction)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success': 'Album Deleted Successfully'}
    return render(request, 'first_app/delete.htm', context=diction)


def delete_artist(request, artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()
    diction = {'delete_success': 'Artist Deleted Successfully'}
    return render(request, 'first_app/delete.htm', context=diction)
