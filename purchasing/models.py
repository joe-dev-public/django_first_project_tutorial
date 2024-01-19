from django.db import models

# Field: first arg = human-readable name, aka:
# https://docs.djangoproject.com/en/4.2/topics/db/models/#verbose-field-names


class Release(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#charfield
    title = models.CharField("release title", max_length=200)
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#datefield
    date = models.DateField("date released")


class Item(models.Model):
    url = models.CharField("item URL", max_length=400)
    total_price = models.DecimalField("total price", max_digits=6, decimal_places=2)
    track_price = models.DecimalField("track price", max_digits=6, decimal_places=2)
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey
    # Not sure I'd actually want deleting a Release to delete an Item, but
    # let's just leave it like this for now.
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
