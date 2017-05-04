from django.db import models

# Create your models here.
class Book(models.Model):

    GENRE_CHOICES = (
        ('FA', 'Fantasy'),
        ('FI', 'Fiction'),
        ('CH', 'Children'),
        ('SF', 'Sci-Fiction'),
        ('RO', 'Romance'),
        ('ME', 'Memoirs'),
        ('SH', 'Self-Help'),
        ('HI', 'History'),
        ('RE', 'Religion'),
        ('BI', 'Biography'),
    )

    name = models.CharField()
    author =
    isbn = models.PositiveIntegerField()
    pub_date = models.DateField()
    cover_photo = models.ImageField()
    description = models.TextField()
    rating = models.FloatField()
    genre = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES,
    )

class Comment(models.Model):
    book =
    user =
    comment_text = models.TextField()
