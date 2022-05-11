from django.db import models
from service.models.vacancy import Vacancy
from service.models.interview import Interview

class Interviewer(models.Model):
    name = models.CharField(max_length=50, null=False)
