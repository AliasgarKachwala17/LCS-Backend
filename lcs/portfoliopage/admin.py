from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CaseStudy)

admin.site.register(Industries)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'type_of_employment', 'experience')