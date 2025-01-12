from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150, unique=True)
    published_Date = models.DateField()  # Ensure this field is present
    Copies_available = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
