from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    number=models.CharField(max_length=12)