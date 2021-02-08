from django.db import models

# Create your models here.
class Bot(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    times_bought = models.IntegerField() 
    