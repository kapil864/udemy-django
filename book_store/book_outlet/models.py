from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):

    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # Adding a foreign key
    # on_delete = models.CASCADE delete book when author is deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    # db_index = True tells DB to index slug field
    # blank = True, allows this field to be blank in django admin panel
    # editable = False , field becomes uneditable in django admin panel
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    # default value is False
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
