from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Des(models.Model):
	#id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Tasks = models.CharField(max_length=200)
	
