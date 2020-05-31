from django.urls import path, include

from .views import dashboar_view

urlpatterns = [
    path('dashboard/', dashboar_view, name='dashboard'),
]
