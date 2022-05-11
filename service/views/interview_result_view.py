from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from service.models.interview_result import InterviewResult

from service.serializers.interview_result_serializer import InterviewResultSerializer
from rest_framework.response import Response


class InterviewResultListCreateAPIView(ListCreateAPIView):
    serializer_class = InterviewResultSerializer
    queryset = InterviewResult.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        created_response = super().create(request, *args, **kwargs)
        if created_response.get("id") is not None:
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response

class InterviewResultRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InterviewResultSerializer
    queryset = InterviewResult.objects.all()