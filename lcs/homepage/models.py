from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class ChooseUs(models.Model):
    logo = models.ImageField(upload_to= 'logos/', blank= True, null= True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.rating} stars)"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"