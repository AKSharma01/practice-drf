from django.db import models
import uuid

# Create your models here.

class Employee(models.Model):
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	address = models.TextField(blank=True, null=True)
	created_at = models.DateField(auto_now_add=True, auto_now=False)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.name