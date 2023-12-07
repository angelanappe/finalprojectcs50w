from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass


class Offer_job(models.Model):

    # status of the job: available or occupied
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('filled', 'Filled'),
    ]

    title = models.CharField(max_length=1000, default="")
    company_name = models.CharField(max_length=1000, default="Reserved")
    company_data = models.CharField(max_length=1000, default="")
    job_description = models.CharField(max_length=1000, default="")
    category = models.CharField(max_length=140, default="")
    location =models.CharField(max_length=1000, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    # for the save/unsave option
    saved_by = models.ManyToManyField(User, related_name='saved_jobs', blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_jobs', null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs', null=True, blank=True)
    
    def __str__(self):
        return f"The job offer made by {self.company_name} was created successfully!"


class User_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400, default="")
    experience = models.CharField(max_length=1000)
    habilities = models.CharField(max_length=1000)
    years = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_applications")
    job = models.ForeignKey(Offer_job, on_delete=models.CASCADE, related_name="job_applied", default="")
    date = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user} applied to {self.job.title} from {self.job.company_name} successfully on {self.date.strftime('%d %b %Y %H:%M:%S')}"
    

class SMS(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    content = models.TextField(default='Default content', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    