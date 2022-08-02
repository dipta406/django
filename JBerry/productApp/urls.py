from django.urls import path
from . import views
urlpatterns = [
    path('trending/',views.trending, name='trending'),
    path('filterByCat/<str:category>/',views.filterByCat, name='filterByCat'),
    path('product_details/<int:pid>/',views.product_details, name='product_details'),
    path('search/',views.search , name = 'search')
]