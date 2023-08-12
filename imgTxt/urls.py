from django.urls import path
from . import views

urlpatterns = [
    path('extract/', views.extract_text_from_image, name='extract_text_from_image'),
    path('extract/api/', views.extract_text_api, name='extract_text_api'),
]
