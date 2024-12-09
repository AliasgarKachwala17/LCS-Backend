from django.db import models

EMPLOYMENT_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Internship', 'Internship'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),

    ]
# Create your models here.
class CaseStudy(models.Model):
    project_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='case_studies/')
    description = models.TextField()
    tags = models.JSONField(default=list)
    

    def __str__(self):
        return self.project_name


class Industries(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='industry/')
    core_services = models.JSONField(default=list)
    unique_challenges = models.JSONField(default=list)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    position_name = models.CharField(max_length=255)
    description = models.TextField()
    experience = models.CharField(max_length=150)
    type_of_employment = models.CharField(max_length=10, choices=EMPLOYMENT_CHOICES,default=EMPLOYMENT_CHOICES[0])

    def __str__(self):
        return self.position_name