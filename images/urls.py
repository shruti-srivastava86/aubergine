from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^upload_images$', views.upload_images, name='upload_images'),
    url(r'^process_images$', views.process_images, name='process_images'),
]