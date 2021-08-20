from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any Kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    Superhost = forms.BooleanField(required=False)
    Instant_book = forms.BooleanField(required=False)
    Amenities = forms.ModelMultipleChoiceField(
        models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple()
    )
    Facilities = forms.ModelMultipleChoiceField(
        models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple()
    )
