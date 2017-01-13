from django.conf.urls import url
from djangoecommerce.accounts.views import register, index, update_user, update_password

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^alterar-dados/$', update_user, name='update_user'),
        url(r'^alterar-senha/$', update_password, name='update_password'),
        url(r'^registro/$', register, name='register'),
        ]