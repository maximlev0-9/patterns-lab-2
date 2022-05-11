from rest_framework import serializers

from service.models.interview_result import InterviewResult


class InterviewResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = '__all__'
