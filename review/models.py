from datetime import datetime
from django.db import models

# Create your models here.
class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    review = models.TextField(max_length=100)
    rating = models.IntegerField()
    suggestion = models.TextField(max_length=100)
    create_at = models.DateTimeField(default=datetime.now)