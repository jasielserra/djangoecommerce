from django.shortcuts import render
from django.views.generic import RedirectView
from djangoecommerce.catalog.models import Product
from .models import CartItem
from django.shortcuts import get_object_or_404
from django.contrib import messages


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(self.request.session.session_key, product)
        if created:
            messages.success(self.request,'Produto Adicionado com Sucesso!!')
        else:
            messages.success(self.request,'Produto Atualizado com Sucesso!!')
        return product.get_absolute_url()

create_cartitem = CreateCartItemView.as_view()