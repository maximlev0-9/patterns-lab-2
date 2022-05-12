from django.db import models

class Interviewer(models.Model):
    name = models.CharField(max_length=50, null=False)
