from django.contrib import admin
from django.contrib import admin
from .models import Employer, JobPosting, JobApplication

class JobPostingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(employer__user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.employer = Employer.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

admin.site.register(Employer)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(JobApplication)
