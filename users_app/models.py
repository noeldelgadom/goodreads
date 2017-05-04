from django.db import models
from genders import GENDER_CHOICES

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    mobile_number = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    library = models.CharField(max_length=128)
