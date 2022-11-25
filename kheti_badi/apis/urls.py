from django.urls import path
from . import views

urlpatterns = [
    path('getData',views.send_data_to_front,name="getData"),
    path('Fert/',views.getFertilizer,name="getFertilizer"),
    path('rain',views.rainfallStatus,name="getFertilizer"),
]

