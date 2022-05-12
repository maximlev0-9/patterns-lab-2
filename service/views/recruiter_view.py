from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from service.models.recruiter import Recruiter

from service.serializers.recruiter_serializer import RecruiterSerializer
from rest_framework.response import Response


class RecruiterListCreateAPIView(ListCreateAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        created_response = super().create(request, *args, **kwargs)
        if created_response.get("company") is not None:
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response

class RecruiterRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()
