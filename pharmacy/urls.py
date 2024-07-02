from django.urls import path
from .views import home, medicine_list, add_medicine, order_medicine

urlpatterns = [
    path('', home, name='home'),
    path('medicines/', medicine_list, name='medicine_list'),
    path('medicines/add/', add_medicine, name='add_medicine'),
    path('medicines/order/', order_medicine, name='order_medicine'),
]
