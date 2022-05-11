from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from service.models.vacancy import Vacancy

# from service.models.user import User
from service.serializers.vacancy_serializer import VacancySerializer
from rest_framework.response import Response


class VacancyListCreateAPIView(ListCreateAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        created_response = super().create(request, *args, **kwargs)
        if created_response.get("company") is not None:
            # user_id = int(request_data.pop('reserved_by_user')[0])
            # book_insurance_to_user(request_serializer, user_id)  # METHOD INJECTION
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response


# def book_insurance_to_user(request_serializer, user_id):
#     user_obj = User.objects.get(id=user_id)
#     request_obj = request_serializer.save()
#     request_obj.synk_insurance_to_user(user_obj, False)
#     request_obj.save()


class VacancyRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
