from django.shortcuts import render
from .models import Student
from .forms import StudentForms
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def index(request):
    form=StudentForms()
    context={'form':form}
    return render(request,'mailssending/index.html',context)


def send(request):
    if request.POST:
        form=StudentForms(request.POST)
        if form.is_valid():
            subjects=form.cleaned_data['subject']
            messages=form.cleaned_data['messages']
            emails=form.cleaned_data['email']
            to_email=[settings.EMAIL_HOST_USER]
            sendMail = send_mail(subject=subjects,from_email=emails,recipient_list=to_email,message=messages,fail_silently=False)
            if sendMail:
                success='Succesfully Sent'
                return render(request,'mailssending/index.html',{'success':success})
    else:
        form=StudentForms()
        return render(request,'mailssending/index.html',{'from':form})
