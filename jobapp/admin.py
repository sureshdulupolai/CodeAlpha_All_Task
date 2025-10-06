from django.contrib import admin
from .models import Employer, Candidate, JobListing, Resume, JobApplication

# Employer Admin
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'website', 'created_at')
    search_fields = ('company_name', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Candidate Admin
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Job Listing Admin
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'salary', 'is_active', 'created_at', 'deadline')
    search_fields = ('title', 'employer__company_name', 'location')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)

# Resume Admin
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'file', 'uploaded_at')
    search_fields = ('candidate__full_name',)
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)

# Job Application Admin
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_at')
    search_fields = ('candidate__full_name', 'job__title')
    list_filter = ('status', 'applied_at')
    ordering = ('-applied_at',)

# Register models with admin
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(JobListing, JobListingAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
