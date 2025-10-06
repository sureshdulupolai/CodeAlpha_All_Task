from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Employer Model
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Employer login
    company_name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name

# Candidate Model
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Candidate login
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

# Job Listing Model
class JobListing(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"

# Resume Model
class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Resume of {self.candidate.full_name}"

# Job Application Model
class JobApplication(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    status_choices = [
        ('APPLIED', 'Applied'),
        ('REVIEW', 'Under Review'),
        ('SHORTLISTED', 'Shortlisted'),
        ('REJECTED', 'Rejected'),
        ('HIRED', 'Hired')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='APPLIED')
    applied_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.candidate.full_name} applied to {self.job.title}"
