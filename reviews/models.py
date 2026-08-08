from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.PROTECT,
        related_name='reviews'
        )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0,'Avalização não pode ser menor que zero'),
            MaxValueValidator(5, 'Avalização não pode ser maior que 5'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie