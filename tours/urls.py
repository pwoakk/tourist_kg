from django.urls import path

from tours.views import get_tour_list

urlpatterns = [
    path('', get_tour_list, name='tour_list'),
]