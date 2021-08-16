from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room-type", 0))

    form = {"city": city, "s_room_type": room_type, "s_country": country}
    choices = {"countries": countries, "room_types": room_types}

    return render(request, "rooms/search.html", context={**form, **choices})
