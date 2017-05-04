from django.db import models
from genres import GENRE_CHOICES
from authors_app.models import Author
from users_app.models import User

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=128)
    author = models.ForeignKey(Author)
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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    comment_text = models.TextField()
