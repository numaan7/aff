from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    description = models.TextField(default="This is an awesomeproduct")
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name
        