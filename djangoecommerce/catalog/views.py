from django.shortcuts import render
from .models import Product, Category
from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'

product_list = ProductListView.as_view()

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {'current_category':category,
               'products': Product.objects.filter(category=category),
               }
    return render(request,'catalog/category.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)