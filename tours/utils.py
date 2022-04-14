from tours.models import RegularTour


def minus_place_count(pk, count):
    try:
        regular_tour = RegularTour.objects.get(id=pk)
        regular_tour.places_count -= count
        regular_tour.save()
    except RegularTour.DoesNotExist:
        return False
