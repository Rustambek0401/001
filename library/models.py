from django.db import models
from student.models import Student

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(auto_now_add=True)

class Book(models.Model):
    title = models.CharField(max_length=203)
    description = models.TextField()
    pric = models.FloatField()
    count = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}, {self.description}"
class BookingBook(models.Model):
    student = models.ManyToManyField(Student)
    book = models.ManyToManyField(Book)
    create_data = models.DateTimeField(auto_now_add=True)
    returen_date = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student}, {self.book}"
class Comments(models.Model):
    text = models.TextField()
    book = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.text}, {self.book}"
