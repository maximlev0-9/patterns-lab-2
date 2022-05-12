from django.db import models

from service.models.candidate import Candidate
from service.models.recruiter import Recruiter


class Vacancy(models.Model):
    position = models.CharField(max_length=20, null=False)
    project_description = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=20, null=False)
    applied_candidates = models.ManyToManyField(Candidate, "applied_vacancies")
    requirements = models.CharField(max_length=200, null=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name="vacancies")