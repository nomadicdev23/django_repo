from django.db import models
from django.db.models import Model
# Create your models here.
  
class Emails(Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 400)

    def __str__(self):  
        return self.email
