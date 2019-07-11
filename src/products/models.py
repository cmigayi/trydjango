from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	desc = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=10000)

	def get_absolute_url(self, *args, **kwargs):
		return reverse("products:product-detail", kwargs={"id": self.id})