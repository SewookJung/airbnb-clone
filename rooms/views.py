from datetime import datetime
from django.shortcuts import render

# Create your views here.


def all_rooms(request):
    now = datetime.now()
    return render(request, "all_rooms.html", context={"now": now})
