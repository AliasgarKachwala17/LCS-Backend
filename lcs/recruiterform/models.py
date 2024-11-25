from django.db import models

# Create your models here.
class ApplicationForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=13)  
    linkedin_profile = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')  
    message = models.TextField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name