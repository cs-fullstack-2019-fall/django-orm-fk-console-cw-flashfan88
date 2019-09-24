from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    date_posted = models.DateTimeField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

