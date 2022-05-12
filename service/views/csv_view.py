import csv

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from service.models.candidate import Candidate
from service.serializers.candidate_serializer import CandidateSerializer


class UploadDataCSVFile(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def create(self, request, *args, **kwargs):
        print(request)
        file = request.data.get("random_data")
        file_rows = [row.decode("utf-8") for row in file]
        reader = csv.reader(
            file_rows, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL
        )
        for candidate_raw in reader:
            if candidate_raw[0] is not "id":
                request_data = format_data(candidate_raw)
                create_request_record(request_data)
        return Response("Uploaded", status=status.HTTP_201_CREATED)


def format_data(insurance):
    request_data = {
        "id": insurance.pop(0),
        "name": insurance.pop(0),
        "phone_number": insurance.pop(0),
        "email": insurance.pop(0),
    }
    return request_data


def create_request_record(request_data):
    candidate_serializer = CandidateSerializer(data=request_data)
    candidate_serializer.is_valid(raise_exception=True)
    request_obj = candidate_serializer.save()

    request_obj.save()

    return True
