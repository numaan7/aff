from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import datetime
class Product(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    description = models.TextField(default="This is an awesomeproduct")
    price = models.IntegerField(default=100)
    image = models.ImageField(storage=S3Boto3Storage(), default=None)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")

    def __str__(self):
        return self.title
        