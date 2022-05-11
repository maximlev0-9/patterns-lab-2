from rest_framework import serializers

from service.models.interviewer import Interviewer


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = '__all__'