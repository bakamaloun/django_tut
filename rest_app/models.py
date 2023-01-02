from django.db import models

# Create your models here.

class RestElements(models.Model):
    rest_text = models.CharField(max_length=200)
    sent = models.BooleanField()