from django.views.generic import ListView, DetailView
from django.shortcuts import render
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
    city = request.GET.get("city")
    city = str.capitalize(city)

    return render(request, "rooms/search.html", context={"city": city})
