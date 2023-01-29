from django.db import models

class Librarian(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    id = models.IntegerField

    def __str__(self):
        return self.title + " " + self.content