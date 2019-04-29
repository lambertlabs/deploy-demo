from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=30, blank=False)
    definition = models.TextField(blank=False)
