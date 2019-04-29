from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=30, blank=False)
    definition = models.TextField(blank=False)

    def get_items(self):
            yield ((f.name, f.value_from_object(self)) for f in Word._meta.get_fields())
