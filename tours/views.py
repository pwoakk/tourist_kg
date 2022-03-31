from django.shortcuts import render

# Create your views here.
from tours.models import Tour


def get_tour_list(request):
    tours = Tour.objects.all()
    context = {
        'tours' : tours,
    }
    return render(request, 'tour_list.html', context=context)