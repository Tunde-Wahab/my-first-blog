from django.db import models
class Dupee(models.Model):
  name=models.TextField()
   
  mydate=models.DateTimeField(auto_now=True)
  mymonth=models.DateField(auto_now=True)
# Create your models here.
