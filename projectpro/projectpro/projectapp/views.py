from django.shortcuts import render
from .models import ServicesData,FeedbackData,ContactData
from .forms import FeedbackForm
import datetime

def home_view(request):
    return render(request, 'home.html')

def services_view(request):
    services=ServicesData.objects.all()
    return render(request, 'services.html',{'services':services})

def contact_view(request):
    if request.method=="POST":
        name=request.POST.get('contactname')
        mobile=request.POST.get('contactmobile')
        email=request.POST.get('contactemail')
        message=request.POST.get('contactmessage')
        currentdate=datetime.datetime.now()
        data=ContactData(name=name,mobile=mobile,email=email,message=message,date=currentdate)
        data.save()

    return render(request, 'contact.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def feedback_view(request):
    if request.method=="POST":
        feedbackform=FeedbackForm(request.POST)
        if feedbackform.is_valid():
            name=request.POST.get('name')
            rating=int(request.POST.get('rating'))
            if rating>=1 and rating<=5:
                rating=rating*('*')
            else:
                rating='None Rating'

            date = datetime.datetime.now()
            msg=request.POST.get('msg')

            feedbacksaving=FeedbackData(feedbackname=name,feedbackrating=rating,
                                        feedbackdate=date,feedbackmsg=msg)
            feedbacksaving.save()
            feedbackform = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request, 'feedback.html', {'feedbacks': feedbacks, 'feedbackform': feedbackform})
    else:
        feedbackform=FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request, 'feedback.html',{'feedbacks':feedbacks,'feedbackform':feedbackform})

