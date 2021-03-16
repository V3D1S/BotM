from django.db import models

# Create your models here.


    


class Bot(models.Model):
	
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=100, blank=False, null=False)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
	description = models.TextField(blank=False, null=False)
	author = models.CharField(max_length=100, blank=False, null=False, default="Admin")
	file = models.FileField(default='bots/no_script.txt', upload_to='bots/uploads')

	class Meta: 
		db_table = 'Bots'
		

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return f"/bot/{self.id}"

