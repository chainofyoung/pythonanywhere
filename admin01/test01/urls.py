    # from django.urls import path
    # from . import views

from django.contrib import admin
from django.urls import path, include
from .views import upload_image,upload_success

urlpatterns = [
   path('upload/', upload_image, name='upload_image'),
    path('upload/success/', upload_success, name='upload_success'),
]