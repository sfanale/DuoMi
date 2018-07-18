from django.db import models

# Create your models here.


class Reporter(models.Model):
	full_name=models.CharField(max_length=70)
	
	def _str_(self):
		return self.full_name
	
class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
	
	def _str_(self):
		return self.headline