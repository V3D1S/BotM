from django.db import models

# Create your models here.
class Bot(models.Model):
	
	title = models.CharField(max_length=100, blank=False, null=False)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
	description = models.TextField(blank=False, null=False)

	class Meta: 
		db_table = 'Bots'
		

	def __str__(self):
		return self.title

