from django.db import models


class Input(models.Model):	
	query = models.CharField(max_length=100)