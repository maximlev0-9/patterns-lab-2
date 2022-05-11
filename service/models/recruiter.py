from django.db import models
from django.apps import apps
# Vacancy = apps.get_model('service', "models.vacancy.Vacancy")

class Recruiter(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=80, null=False)
    # vacancies = models("service.Vacancy", on_delete=models.CASCADE, related_name="vacancy")