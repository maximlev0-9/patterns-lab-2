from rest_framework import serializers

from service.models.candidate import Candidate
# from service.serializers.experience_serializer import ExperienceSerializer
from service.serializers.interview_result_serializer import InterviewResultSerializer
from service.serializers.vacancy_serializer import VacancySerializer


class CandidateSerializer(serializers.ModelSerializer):
    interview_results = InterviewResultSerializer(many=True, required=False)
    applied_vacancies = VacancySerializer(many=True, required=False)
    class Meta:
        model = Candidate
        fields = '__all__' 