from django.db import models

class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_duration=models.CharField(max_length=100)
    course_startdate=models.DateField(max_length=100)
    course_starttime=models.TimeField()
    course_trainername=models.CharField(max_length=100)
    course_trainerexp=models.CharField(max_length=100)

class FeedbackData(models.Model):
    feedbackname=models.CharField(max_length=100)
    feedbackrating=models.CharField(max_length=100)
    feedbackdate=models.DateTimeField(max_length=100)
    feedbackmsg=models.TextField(max_length=100)

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=100)