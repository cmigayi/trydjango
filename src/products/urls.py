from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view
from products.views import (
	product_detail, 
	product_create, 
	product_edit,
	product_delete)

app_name = 'products'

urlpatterns = [
	path('detail/<int:id>/', product_detail, name='product-detail'),
	path('create/', product_create, name="product-create"),
	path('edit/', product_edit, name="product-edit"),
	path('delete/<int:id>/delete/', product_delete, name="product-delete"),
]