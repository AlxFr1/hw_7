from django.urls import path

from .views import triangle

urlpatterns = [
    path('', triangle)
]
