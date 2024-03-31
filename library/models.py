from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=203)
    description = models.TextField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title}, {self.description}"