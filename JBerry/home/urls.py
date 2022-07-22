from django.urls import path
from home import views
urlpatterns = [
    path('',views.index, name='home'),
    path('register/',views.register, name='register'),
    path('login',views.Login, name='login'),
    path('logout',views.Logout, name='logout'),
]

