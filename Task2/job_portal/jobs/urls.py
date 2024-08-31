from django.urls import path
from .views import JobPostingListView, JobPostingCreateView, JobApplicationCreateView

urlpatterns = [
    path('jobs/', JobPostingListView.as_view(), name='job-list'),
    path('jobs/create/', JobPostingCreateView.as_view(), name='job-create'),
    path('jobs/apply/', JobApplicationCreateView.as_view(), name='job-apply'),
]
