from django.urls import path
from . import views

urlpatterns = [
    path('extract/', views.extract_text_from_image, name='extract_text'),
    path('api/extract/<str:image_url>/', views.extract_text_api, name='extract_text_api'),
]
