from django.shortcuts import render
from django.core.mail import send_mail

def main(request):
    return render(request , 'index.html')

def send(request):
    message = request.POST.get('textarea')
    send_mail(
    'Message from personal-site',
    message,
    None,
    ['peymanpic00@gmail.com'],
    fail_silently=False,
)