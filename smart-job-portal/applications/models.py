from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job

class Application(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    resume=models.FileField(upload_to='applications/resumes/')
    cover_letter=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"