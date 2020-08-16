from django.db import models

# Create your models here.


class TodoList(models.Model):

    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):

        return self.name