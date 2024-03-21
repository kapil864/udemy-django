from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=50, null=True)

    # default value is False
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])
    