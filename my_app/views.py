from django.shortcuts import render
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import contectus
from .signal import message_sent
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        mail = request.POST.get('email')
        subj = request.POST.get('subject')
        msg = request.POST.get('message')
        contact = contectus(name=Name, email=mail, subject=subj, messages=msg)
        contact.save()

        # Send the signal
        message_sent.send(sender=request, name=Name, email=mail, subject=subj, messages=msg)

        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')


    return render(request, 'index.html')




def resume(request):

    return render(request,'resume.html')

