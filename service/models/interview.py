from django.db import models
from service.models.candidate import Candidate
from service.models.vacancy import Vacancy
from service.models.interviewer import Interviewer
from service.models.recruiter import Recruiter

class Interview(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="upcoming_interviews")
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE, related_name='upcoming_interviews')
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='upcoming_interviews')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=False)
    time = models.DateTimeField()