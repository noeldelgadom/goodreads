from django.db import models
from nationalities import NATIONALITIES
from genres import GENRE_CHOICES
from genders import GENDER_CHOICES

# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    nationality = models.CharField(
        max_length=2,
        choices=NATIONALITIES,
    )
    biography = models.TextField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    genre = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES,
    )
    age = models.PositiveIntegerField()
    alive = models.BooleanField()
