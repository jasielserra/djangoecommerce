from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

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
   #else:
   #    form = ContactForm()

    context = {
        'form':form,
        'success':success
    }
    return render(request,'contact.html', context)

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')

register = RegisterView.as_view()