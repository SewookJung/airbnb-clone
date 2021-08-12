from django.shortcuts import render
from django.core.paginator import Paginator

from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    room_obj = paginator.get_page(page)
    print(dir(room_obj.paginator))

    return render(
        request,
        "rooms/home.html",
        context={"room_obj": room_obj},
    )
