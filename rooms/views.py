from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator

from . import models
from . import forms


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


class SearchView(View):
    """SearchView Definition"""

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                bedrooms = form.cleaned_data.get("bedrooms")
                superhost = form.cleaned_data.get("superhost")
                instant_book = form.cleaned_data.get("instant_book")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type:
                    filter_args["room_type"] = room_type

                if price:
                    filter_args["price__lte"] = price

                if guests:
                    filter_args["guests__gte"] = guests

                if bedrooms:
                    filter_args["bedrooms__gte"] = bedrooms

                if baths:
                    filter_args["baths__gte"] = baths

                if beds:
                    filter_args["beds__gte"] = beds

                if instant_book is True:
                    filter_args["instant_book"] = instant_book

                if superhost is True:
                    filter_args["host__superhost"] = superhost

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                for amenity in amenities:
                    qs = qs.filter(amenities=amenity)

                for facility in facilities:
                    qs = qs.filter(facilities=facility)

                page = request.GET.get("page", 1)
                paginator = Paginator(qs, 10, orphans=5)
                rooms = paginator.get_page(page)

                return render(
                    request,
                    "rooms/search.html",
                    context={
                        "form": form,
                        "rooms": rooms,
                    },
                )

        else:
            form = forms.SearchForm()

        return render(
            request,
            "rooms/search.html",
            context={"form": form},
        )
