from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150, unique=True)
    published_Date = models.DateField()  
    Copies_available = models.PositiveBigIntegerField()
    image_address=models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
