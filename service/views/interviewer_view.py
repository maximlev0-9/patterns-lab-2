from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from service.models.interviewer import Interviewer

from service.serializers.interviewer_serializer import InterviewerSerializer
from rest_framework.response import Response


class InterviewerListCreateAPIView(ListCreateAPIView):
    serializer_class = InterviewerSerializer
    queryset = Interviewer.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        created_response = super().create(request, *args, **kwargs)
        if created_response.get("id") is not None:
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response

class InterviewerRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InterviewerSerializer
    queryset = Interviewer.objects.all()
