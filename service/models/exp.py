
from django.db import models
from service.models.candidate import Candidate

class Experience(models.Model):
    since = models.DateTimeField(null=False)
    to = models.DateTimeField(null=False)

    general_description = models.CharField(max_length=200, null=True)
    responsibilities = models.CharField(max_length=200, null=True)
    technologies_used = models.JSONField([])
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)