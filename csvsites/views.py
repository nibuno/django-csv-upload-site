from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UploadFileForm
from .models import Music
import os
import csv
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def index(request):
    return render(request, 'csvsites/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved. by binary
            f = request.FILES['file']
            path = os.path.join(UPLOAD_DIR, f.name)
            with open(path, 'wb') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            # open csv
            with open(path, 'r') as destination:
                # read csv
                rdr = csv.reader(destination)
                # insert
                for r in rdr:
                    music = Music()
                    music.music_title = r[0]
                    music.artist_names = r[1]
                    music.album_name = r[2]
                    music.release_date = r[3]
                    music.save()
            return redirect('index')
    else:
        # GET
        form = UploadFileForm()
    return render(request, 'csvsites/upload.html', {'form': form})


class MusicList(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Music.objects.filter(
                Q(music_title__icontains=q_word) | Q(artist_names__icontains=q_word) |
                Q(album_name__icontains=q_word) | Q(release_date__icontains=q_word))
        else:
            object_list = Music.objects.all()
        return object_list
