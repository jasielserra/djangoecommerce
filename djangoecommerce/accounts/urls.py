from django.conf.urls import url
from djangoecommerce.accounts.views import register

urlpatterns = [
        url(r'^registro/$', register, name='register')
        ]