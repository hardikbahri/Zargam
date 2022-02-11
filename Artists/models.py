from django.db import models

class Artist(models.Model):
    full_name = models.CharField(max_length=15)

    image = models.ImageField()
    def __str__(self):
        return self.full_name
# Create your models here.
