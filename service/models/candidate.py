from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=80, null=False)