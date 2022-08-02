from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:uid>/', views.viewCart, name='ViewCart'),
]