from django.db import models

# TODO todo to do
class InterviewResult(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=80, null=False)
