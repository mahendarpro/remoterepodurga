from django.contrib import admin
from .models import ServicesData

class AdminServicesData(admin.ModelAdmin):
    list_display = ['course_id','course_name','course_duration','course_startdate',
                    'course_starttime','course_trainername','course_trainerexp']

admin.site.register(ServicesData,AdminServicesData)