from django.db import models

class Recruiter(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=80, null=False)