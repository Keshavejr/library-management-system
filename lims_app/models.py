from django.db import models
from django.db.models import TextField

# Create your models here.
class Reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.CharField(max_length=255, default='Unknown')
    active=models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=255)
    available_copies = models.IntegerField()
    isbn = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=255)
    book = models.CharField(max_length=255)
    date_borrowed = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

class Borrowing(models.Model):
    name = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    date_borrowed = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.book}"





