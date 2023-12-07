from django import forms
from django.db.models import Q, Subquery
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from .forms import RegisterForm, ProfileForm, JobForm, EditProfileForm, ApplicationForm
from .models import User, User_profile, Application, SMS, Offer_job


def index(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == 'search':
            # Redirect user to search_jobs page
            return redirect('search_jobs')
        elif choice == 'offer':
            # Redirect user to post_job page
            return redirect('post_job')
    
    jobs = Offer_job.objects.filter(status='available')
    return render(request, 'joboffers/index.html', {
        "jobs": jobs
    })


@login_required
def search_jobs(request):
    # Retrieve and display available jobs
    jobs = Offer_job.objects.filter(status='available').order_by('id').reverse()

    # Retrieve the jobs that the user has applied for
    user_applied_jobs = Application.objects.filter(user=request.user).values('job')

    # Exclude the jobs that the user has applied for
    applied_jobs = jobs.exclude(id__in=user_applied_jobs)

    # Pagination
    paginator = Paginator(applied_jobs, 7)  # Show 7 jobs per page

    page = request.GET.get('page')
    try:
        jobs_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs_page = paginator.page(paginator.num_pages)

    return render(request, 'joboffers/search_jobs.html', {
        'jobs': jobs_page,
    })

    return render(request, 'joboffers/search_jobs.html', {
        'jobs': applied_jobs,
    })


@login_required
def post_job(request):
    if request.method == 'POST':
        # to handle the form submission for posting a job
        form = JobForm(request.POST)
        if form.is_valid():
            form.instance.status = 'available'
            job = form.save(commit=False)
            job.status = 'available'
            job.created_by = request.user
            job.posted_by = request.user
            job.save()
            print("Job posted successfully")
            return redirect('search_jobs')
        else:
            print(form.errors)

    else:
        # Display the form for posting a job
        form = JobForm()

    return render(request, 'joboffers/post_job.html', {
        'form': form
    })


def job_detail(request, job_id): 
    job = get_object_or_404(Offer_job, pk=job_id)
    applications = Application.objects.filter(job=job)

    if request.method == 'POST':
        # Check if the job is already saved by the user
        if request.user in job.saved_by.all():
            # If saved, remove from saved jobs
            job.saved_by.remove(request.user)
        else:
            # If not saved, add to saved jobs
            job.saved_by.add(request.user)

    # exclude jobs for which user already applied
    applied_jobs = Application.objects.filter(user=request.user, job=job).exists()

    return render(request, 'joboffers/job_detail.html', {
        'job': job,
        'applications': applications,
        'applied_jobs': applied_jobs,
    })


def register(request):

    if request.method == "POST":
        current_username = request.POST["username"]
        current_email = request.POST["email"]
        current_password = request.POST["password"]
        c_confirmation = request.POST["confirmation"]

        print(f"Username: {current_username}")
        print(f"Email: {current_email}")
        print(f"Password: {current_password}")
        print(f"Confirmation: {c_confirmation}")

        # Ensure password matches confirmation
        if current_password != c_confirmation:
            return render(request, "joboffers/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create a new user
        try:
            new_user = User.objects.create_user(current_username, current_email, current_password)
            print(f"User created successfully")
        except IntegrityError:
            print(f"Username already taken.")
            return render(request, "joboffers/register.html", {
                "message": "Username already taken."
            })

        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "joboffers/register.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect': reverse("index")})
        else:
           return JsonResponse({'success': False}, status=400)
    else:
        return render(request, "joboffers/login.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def profile(request):
   # current logged in user
    current_user = request.user

    try:
        user_profile = User_profile.objects.get(user=current_user)
    except User_profile.DoesNotExist:
        user_profile = None

    # Retrieve applications for the current user
    applications = Application.objects.filter(user=current_user)

    # Retrieve posted jobs made by user
    owner_job = Offer_job.objects.filter(created_by=current_user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.instance.user = current_user
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, "joboffers/my_profile.html", {
        "current_user": current_user,
        "form": form,
        "user_profile": user_profile,
        "applications": applications,
        "owner_job": owner_job,
    })


@login_required
def edit_profile(request):
    current_user = request.user

    try:
        user_profile = User_profile.objects.get(user=current_user)
    except User_profile.DoesNotExist:
        user_profile = None

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, "joboffers/edit_profile.html", {
        "form": form
    })


def step1(request, job_id):
    # step 1: display the form for job selection
    current_user = request.user

    # Check if User_profile exists, if not, create user_profile
    try:
        user_profile = User_profile.objects.get(user=current_user)
    except User_profile.DoesNotExist:
        # if user_profile doesn't exist, create one
        user_profile = User_profile.objects.create(user=current_user)

    # Retrieve the job
    job = get_object_or_404(Offer_job, pk=job_id)

    # Display the form for job selection
    form = ApplicationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            request.session['job_id'] = form.cleaned_data['job'].id
            return redirect('step2')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'joboffers/step1.html', {
        'form': form,
        'job': job,
        'user_profile': user_profile,
    })

def step2(request, job_id):
    # step 2: display user information for confirmation
    job = get_object_or_404(Offer_job, id=job_id)
    current_user = request.user

    # Check if User_profile exists
    try:
        user_profile = User_profile.objects.get(user=current_user)
    except User_profile.DoesNotExist:
        # If not, create one
        user_profile = User_profile.objects.create(user=current_user)

    return render(request, 'joboffers/step2.html', {
        'job': job,
        'user_profile': user_profile
    })

def confirm_application(request, job_id):
    # step 3: process the application
    job = Offer_job.objects.get(id=job_id)

    # Additional logic to save the application
    user_profile = User_profile.objects.get(user=request.user)
    application = Application.objects.create(user=request.user, job=job, user_profile=user_profile)

    # Clear session data
    request.session.pop('job_id', None)

    return render(request, 'joboffers/confirm_application.html', {
        'job': job,
        'application': application,
    })


@login_required
def remove_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    # Check if the application belongs to the current user
    if application.user == request.user:
        application.delete()

    return redirect('profile')


def send_message(request, receiver_id):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        sender = request.user
        receiver = User.objects.get(pk=receiver_id)
        
        SMS.objects.create(sender=sender, receiver=receiver, content=content)

        messages.success(request, 'Message sent successfully!')
        return redirect('inbox')  # Redirect to your inbox or message list page

    return render(request, 'joboffers/send_message.html')


def delete_message(request, message_id):
    message = get_object_or_404(SMS, pk=message_id)

    # Check if the user has permission to delete the message
    if request.user == message.sender:
        message.is_deleted = True
        message.save()

    return redirect('inbox')


def inbox(request):
    user = request.user
    messages = SMS.objects.filter(Q(sender=user) | Q(receiver=user)).order_by('-timestamp')
    

    # Mark messages as read when they are displayed
    for message in messages:
        if not message.is_read and message.receiver == user:
            message.is_read = True
            message.save()
    
    unread_messages = messages.filter(receiver=user, is_read=False).exists()

    return render(request, 'joboffers/inbox.html', {
        'messages': messages,
        'unread_messages': unread_messages,
    })


def saved_jobs(request):
    saved_jobs = request.user.saved_jobs.all()
    #exclude jobs for which user already applied
    applied_jobs = Application.objects.filter(user=request.user).values_list('job', flat=True)
    saved_jobs = saved_jobs.exclude(id__in=applied_jobs)
    return render(request, 'joboffers/saved_jobs.html', {
        'saved_jobs': saved_jobs
    })


@login_required
def save_job(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        job = Offer_job.objects.get(pk=job_id)

        if request.user in job.saved_by.all():
            job.saved_by.remove(request.user)
            saved = False
        else:
            job.saved_by.add(request.user)
            saved = True

        return JsonResponse({
            'saved': saved
        })
    

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Offer_job, id=job_id)

    # Check if the logged-in user is the owner of the job
    if request.user == job.created_by:
        job.delete()
        print("Job deleted successfully")
    else:
        print("You are not the owner of this job")

    return redirect('profile')

@login_required
def candidates(request, job_id):
    job = get_object_or_404(Offer_job, id=job_id)
    applications = Application.objects.filter(job=job)
    return render(request, 'joboffers/candidates.html', {
        "applications": applications, 
        "job": job
    })