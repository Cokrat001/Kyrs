from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create_customer', views.create_customer),
    path('create_card', views.create_card),
    path('deactivate_card', views.deactivate_card),

]
