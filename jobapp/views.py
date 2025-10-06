from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobListing, JobApplication, Resume, Employer, Candidate
from django.contrib.auth.models import User

def job_list(request):
    jobs = JobListing.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'job/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    return render(request, 'job/job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    candidate = get_object_or_404(Candidate, user=request.user)

    if request.method == "POST":
        resume_file = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter', '')

        # Save resume
        resume = Resume.objects.create(candidate=candidate, file=resume_file)

        # Create job application
        JobApplication.objects.create(
            candidate=candidate,
            job=job,
            resume=resume,
            cover_letter=cover_letter
        )

        return render(request, 'job/application_success.html', {'job': job})

    resumes = Resume.objects.filter(candidate=candidate)
    return render(request, 'job/apply_job.html', {'job': job, 'resumes': resumes})

@login_required
def add_job(request):
    try:
        employer = request.user.employer  # fetch employer linked to User
    except Employer.DoesNotExist:
        return render(request, 'job/error.html', {'message': 'You are not registered as an Employer.'})

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary = request.POST.get('salary', '')
        deadline = request.POST.get('deadline', None)

        JobListing.objects.create(
            employer=employer,
            title=title,
            description=description,
            location=location,
            salary=salary,
            deadline=deadline
        )
        return redirect('jobapp:job_list')

    return render(request, 'job/add_job.html')

@login_required
def post_job(request):
    employer = get_object_or_404(Employer, user=request.user)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary = request.POST.get('salary', '')
        deadline = request.POST.get('deadline', None)

        JobListing.objects.create(
            employer=employer,
            title=title,
            description=description,
            location=location,
            salary=salary,
            deadline=deadline
        )
        return render(request, 'job/post_success.html', {'title': title})

    return render(request, 'job/post_job.html')
