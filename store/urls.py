from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    # homepage
    path('', views.all_products, name='all_products'),
    # individual item page
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    # individual category page
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    
]