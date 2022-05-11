# import csv

# from rest_framework import status
# from rest_framework.generics import ListCreateAPIView
# from rest_framework.response import Response

# from service.models.vacancy import Vacancy
# from service.serializers.insurance_data_serializer import InsuranceDataSerializer


# class UploadDataCSVFile(ListCreateAPIView):
#     serializer_class = InsuranceDataSerializer
#     queryset = InsuranceData.objects.all()

#     def create(self, request, *args, **kwargs):
#         print(request)
#         file = request.data.get('insurance_data')
#         file_rows = [row.decode("utf-8") for row in file]
#         reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
#         for service in reader:
#             if insurance:
#                 request_data = format_data(insurance)
#                 create_request_record(request_data)  # METHOD INJECTION
#         return Response('Uploaded', status=status.HTTP_201_CREATED)


# def format_data(insurance):
#     request_data = {"id": insurance.pop(0),
#                     "condition": insurance.pop(0),
#                     "country": insurance.pop(0),
#                     "price": insurance.pop(0),
#                     "is_available": bool(insurance.pop(0)),
#                     "title": insurance.pop(0),
#                     "reserved by user": insurance.pop(0)}

#     return request_data


# def create_request_record(request_data):
#     insurance_serializer = InsuranceDataSerializer(data=request_data)
#     insurance_serializer.is_valid(raise_exception=True)
#     request_obj = insurance_serializer.save()

#     request_obj.save()

#     return True
