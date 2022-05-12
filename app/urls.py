
from django.contrib import admin
from django.urls import path

from service.views.candidate_view import CandidateListCreateAPIView, CandidateRetrieveUpdateAPIView
from service.views.csv_view import UploadDataCSVFile
from service.views.interview_view import InterviewListCreateAPIView, InterviewRetrieveUpdateAPIView
from service.views.interview_result_view import InterviewResultListCreateAPIView, InterviewResultRetrieveUpdateAPIView
from service.views.interviewer_view import InterviewerListCreateAPIView, InterviewerRetrieveUpdateAPIView
from service.views.vacancy_view import VacancyListCreateAPIView, VacancyRetrieveUpdateAPIView
from service.views.recruiter_view import RecruiterListCreateAPIView, RecruiterRetrieveUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('candidates/', CandidateListCreateAPIView.as_view()),
    path('candidates/<int:pk>/', CandidateRetrieveUpdateAPIView.as_view()),

    path('interviews/', InterviewListCreateAPIView.as_view()),
    path('interviews/<int:pk>/', InterviewRetrieveUpdateAPIView.as_view()),

    path('interviewers/', InterviewerListCreateAPIView.as_view()),
    path('interviewers/<int:pk>/', InterviewerRetrieveUpdateAPIView.as_view()),

    path('interview_results/', InterviewResultListCreateAPIView.as_view()),
    path('interview_results/<int:pk>/', InterviewResultRetrieveUpdateAPIView.as_view()),

    path('vacancies/', VacancyListCreateAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateAPIView.as_view()),

    path('recruiters/', RecruiterListCreateAPIView.as_view()),
    path('recruiters/<int:pk>/', RecruiterRetrieveUpdateAPIView.as_view()),

    path('test_csv/', UploadDataCSVFile.as_view()),
]