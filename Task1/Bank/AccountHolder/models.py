from django.db import models

class AccountHolder(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    NID = models.CharField(max_length=10)