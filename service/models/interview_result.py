from django.db import models

from service.models.candidate import Candidate
from service.models.vacancy import Vacancy

class InterviewResult(models.Model):
    time = models.DateTimeField("time of interview", auto_now=True)
    percentage_of_correct_questions = models.SmallIntegerField("percentage of correct questions",null=False)
    overall_estimation = models.SmallIntegerField("overall estimation")
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="interview_results")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
