from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import contectus
from .signal import message_sent
from django.contrib import messages
from django.http import FileResponse
import os
from django.conf import settings


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

        messages.success(request, 'Your message has been sent successfully!')

        # Redirect to the same page to avoid resubmission on refresh
        return redirect('index')

    return render(request, 'index.html')



def download_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'my_app/static/samiullahjabbar.pdf')  # Update this path
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise FileNotFoundError(f"{file_path} not found")