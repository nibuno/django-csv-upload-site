from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.MusicList.as_view(), name='music'),
    path('upload/', views.upload, name='upload'),
]
