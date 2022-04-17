from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_files.html', views.upload, name='upload'),
    path('download_files.html', views.download, name='download')
]
