from rest_framework import generics
from .models import JobPosting, JobApplication
from .serializers import JobPostingSerializer, JobApplicationSerializer
from django.utils import timezone

class JobPostingListView(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

    def get_queryset(self):
        return JobPosting.objects.filter(expiry_date__gte=timezone.now())

class JobPostingCreateView(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
