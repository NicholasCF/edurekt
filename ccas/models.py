from django.db import models


# Create your models here.
class Cca(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    description = models.TextField(blank=False)

    def __str__(self):
        return "{}".format(self.name)
