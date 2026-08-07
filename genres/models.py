from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __set__(self):
        return self.name