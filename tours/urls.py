from django.urls import path

from tours.views import get_tour_list, get_tour_detail, create_booking_tour

urlpatterns = [
    path('', get_tour_list, name='tour_list'),
    path('tour/<int:pk>/', get_tour_detail, name='tour_detail'),
    path('tour/booking/<int:tour_pk>/', create_booking_tour, name='booking'),
]