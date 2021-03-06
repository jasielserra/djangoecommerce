from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm

User = get_user_model()

class IndexView(TemplateView):
    template_name ='index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
   #else:
   #    form = ContactForm()

    context = {
        'form':form,
        'success':success
    }
    return render(request,'contact.html', context)


