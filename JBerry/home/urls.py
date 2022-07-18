from django.urls import path
from home import views
urlpatterns = [
    path('',views.index, name='home'),
     path('register',views.register, name='register'),
     
]
