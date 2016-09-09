from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name,email,message)
            send_mail(
                'Contato do Django E-Commerce', message, settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            success = True

    else:
        form = ContactForm()

    context = {
        'form':form,
        'success':success
    }
    return render(request,'contact.html', context)


