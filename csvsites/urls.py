from django.urls import path

from . import views


urlpatterns = [
    path('', views.MusicList.as_view(), name='music'),
    path('upload/', views.upload, name='upload'),
]
