from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:uid>/', views.viewCart, name='viewCart'),
     path('addToCart/', views.addToCart, name='addToCart'),
]