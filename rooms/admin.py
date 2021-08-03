from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rule",
                )
            },
        ),
        (
            "More About the Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "baths",
                    "bedrooms",
                )
            },
        ),
        ("Last Details", {"fields": (
            "host",
        )})
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
    )

    list_filter = (
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "country",
        "city",
        "instant_book",
    )

    search_fields = ["city", "host__username"]
    filter_horizontal = [
        "amenities",
        "facilities",
        "house_rule",
    ]


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
