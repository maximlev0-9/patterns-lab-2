from rest_framework import serializers

from service.models.recruiter import Recruiter
from service.serializers.vacancy_serializer import VacancySerializer


class RecruiterSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, required=False)

    class Meta:
        model = Recruiter
        fields = '__all__'
