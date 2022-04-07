from django.http import Http404
from django.shortcuts import render

# Create your views here.
from tours.models import Tour


def get_tour_list(request):
    tours = Tour.objects.all()
    context = {
        'tours' : tours,
    }
    return render(request, 'tour_list.html', context=context)


def get_tour_detail(request, pk):
    try:
        tour = Tour.objects.get(id=pk)
    except Tour.DoesNotExist:
        raise Http404
    context = {
        "tour": tour,
    }
    return render(request, 'tour_detail.html', context=context)