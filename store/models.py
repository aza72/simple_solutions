from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name