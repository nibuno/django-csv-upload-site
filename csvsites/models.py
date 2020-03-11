from django.db import models


class Music(models.Model):
    music_title = models.CharField(max_length=100)
    artist_names = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField('music released')

    # upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.music_title
