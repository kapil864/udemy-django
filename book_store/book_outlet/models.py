from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=50, null=True)
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

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
