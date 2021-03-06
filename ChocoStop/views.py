# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Category, Product


# @login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'ChocoStop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# @login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'ChocoStop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def product_add_to_cart(request, id):
    category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, available=True)
    products = Product.objects.filter(available=True)
    cart = Cart(request)
    cart.add(product=product,
             quantity=1,
             override_quantity=False)
    return render(request,
                  'ChocoStop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_add_to_cart_with_category(request, id, category_slug):
    category = category_slug
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, available=True)
    products = Product.objects.filter(available=True)
    cart = Cart(request)
    cart.add(product=product,
             quantity=1,
             override_quantity=False)
    return render(request,
                  'ChocoStop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
