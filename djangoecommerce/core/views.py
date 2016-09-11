from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request,'index.html')

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    else:
        form = ContactForm()

    context = {
        'form':form,
        'success':success
    }
    return render(request,'contact.html', context)


