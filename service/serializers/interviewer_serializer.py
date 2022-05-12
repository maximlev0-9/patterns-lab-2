from rest_framework import serializers

from service.models.interviewer import Interviewer
from service.serializers.interview_serializer import InterviewSerializer


class InterviewerSerializer(serializers.ModelSerializer):
    upcoming_interviews = InterviewSerializer(many=True, required=False)
    class Meta:
        model = Interviewer
        fields = '__all__'
