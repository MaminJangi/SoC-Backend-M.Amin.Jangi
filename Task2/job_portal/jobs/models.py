from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()

    def __str__(self):
        return self.company_name

class JobPosting(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)
    expiry_date = models.DateField()
    category = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    working_hours = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
