from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # This option is not migration in database
        abstract = True
