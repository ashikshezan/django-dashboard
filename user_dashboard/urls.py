from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import dashboar_view

urlpatterns = [
    path('', dashboar_view, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls'))
]
