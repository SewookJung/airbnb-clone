from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANG_EN = "en"
    LANG_KR = "kr"

    LANG_CHOICES = (
        (LANG_EN, "English"),
        (LANG_KR, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(blank=True)
    birth = models.DateField(blank=True, null=True)
    lang = models.CharField(choices=LANG_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
