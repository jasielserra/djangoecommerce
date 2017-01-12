from django.conf.urls import url
from djangoecommerce.accounts.views import register, index

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^registro/$', register, name='register'),
        ]