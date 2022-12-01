from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Product


# homepage
def product_all(request):
    # collect active products from DB
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


# return individual item by slug
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


# return items by individual category slug
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})