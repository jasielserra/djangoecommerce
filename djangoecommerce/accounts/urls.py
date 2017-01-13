from django.conf.urls import url
from djangoecommerce.accounts.views import register, index, update_user

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^alterar-dados/$', update_user, name='update_user'),
        url(r'^registro/$', register, name='register'),
        ]