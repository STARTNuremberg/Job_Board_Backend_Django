from django.contrib import admin
from django.urls import path
from api.views import JobPostingAPI, JobPostingDetailsAPI

urlpatterns = [
    path("jobs/job-posting/", JobPostingAPI.as_view()),
    path("jobs/job-posting/<int:job_id>/", JobPostingDetailsAPI.as_view()),
]
