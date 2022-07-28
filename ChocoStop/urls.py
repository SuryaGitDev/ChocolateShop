from django.urls import path, include
from . import views
app_name = 'ChocoStop'
urlpatterns = [
 path('', views.product_list, name='product_list'),
 path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
 path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
 path('add/<int:id>', views.product_add_to_cart, name='product_add_to_cart'),
 path('category_slug/add/<int:id>', views.product_add_to_cart_with_category, name='product_add_to_cart_with_category'),
]