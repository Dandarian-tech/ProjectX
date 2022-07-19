from django.shortcuts import render, get_object_or_404
from matplotlib.style import available
from matplotlib.widgets import Widget
from cart.forms import CartAddProductForm
from .models import *

# Create your views here.
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    laptops = Product.objects.filter(category=1).order_by('id')[:4]
    speakers = Product.objects.filter(category=2)
    # screens = Product.objects.filter(categories.name=='screen')
    latest = products.order_by('-id')[:6]
    cart_product_form = CartAddProductForm()
    context = {
        'products':products, 
        'categories':categories, 
        'laptops':laptops, 
        'speakers':speakers, 
        'latest':latest,
        'cart_product_form': cart_product_form
        }
    return render(request, 'product/index.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product, 
        'cart_product_form': cart_product_form
        }
    return render(request, 'product/detail.html', context)

def products(request):
    products = Product.objects.filter(available=True)
    context={
        'products':products
    }
    return render(request, 'product/products.html', context)