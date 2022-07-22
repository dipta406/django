from django.urls import path
from . import views
urlpatterns = [
    path('trending/',views.trending, name='trending'),
]