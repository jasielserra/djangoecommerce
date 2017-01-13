from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from djangoecommerce.accounts.forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

class UpdateUserView(LoginRequiredMixin,UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name','email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


update_user = UpdateUserView.as_view()
index = IndexView.as_view()
register = RegisterView.as_view()

