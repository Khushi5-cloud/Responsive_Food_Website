from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('order',views.order,name='order'),
    path('recipe',views.recipe,name='recipe'),
]