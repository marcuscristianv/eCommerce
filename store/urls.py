from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    # homepage
    path('', views.product_all, name='product_all'),
    # individual item page
    path('<slug:slug>', views.product_detail, name='product_detail'),
    # individual category page
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]