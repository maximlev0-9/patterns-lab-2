"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from service.views.candidate_view import CandidateListCreateAPIView, CandidateRetrieveUpdateAPIView

# from service.views.csv_view import UploadDataCSVFile
from service.views.experience_view import ExperienceListCreateAPIView, ExperienceRetrieveUpdateAPIView
from service.views.vacancy_view import VacancyListCreateAPIView, VacancyRetrieveUpdateAPIView
from service.views.recruiter_view import RecruiterListCreateAPIView, RecruiterRetrieveUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),



    path('candidates/', CandidateListCreateAPIView.as_view()),
    path('candidates/<int:pk>/', CandidateRetrieveUpdateAPIView.as_view()),

    path('experiences/', ExperienceListCreateAPIView.as_view()),
    path('experiences/<int:pk>/', ExperienceRetrieveUpdateAPIView.as_view()),

    path('interviews/', VacancyListCreateAPIView.as_view()),
    path('interviews/<int:pk>/', VacancyRetrieveUpdateAPIView.as_view()),

    path('interviewers/', VacancyListCreateAPIView.as_view()),
    path('interviewers/<int:pk>/', VacancyRetrieveUpdateAPIView.as_view()),

    path('vacancies/', VacancyListCreateAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateAPIView.as_view()),

    path('recruiters/', RecruiterListCreateAPIView.as_view()),
    path('recruiters/<int:pk>/', RecruiterRetrieveUpdateAPIView.as_view()),

    # path('test_csv/', UploadDataCSVFile.as_view()),
]
