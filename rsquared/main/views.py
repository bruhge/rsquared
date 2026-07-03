from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html', {'active': 'home'})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Query from {name}'
        body = f'Email from {email},\n\n{message}'
        send_mail(
            subject=subject,
            message=body,
            from_email='bruhge@gmail.com',
            recipient_list=['bruhge@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Thank you for submitting!  Your message has been sent.')
        return redirect('home')
    return render(request, 'main/contact.html', {'active': 'contact'})

def evaluations(request):
    return render(request, 'main/evaluations.html', {'active': 'evaluations'})

def therapy(request):
    return render(request, 'main/therapy.html', {'active': 'therapy'})

def speciality(request):
    return render(request, 'main/specialities.html', {'active': 'specialities'})

def modalities(request):
    return render(request, 'main/modalities.html', {'active': 'modalities'})