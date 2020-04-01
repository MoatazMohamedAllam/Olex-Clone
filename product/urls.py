from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index,name='index'),
    path('add_advertise', views.add_advertise,name='add_advertise'),
    path('all_products', views.product_list,name='product_list'),
    path('all_products/search', views.search,name='search'),
    path('all_products/<slug:category_slug>', views.product_list,name='product_list_category'),
    path('<slug:product_slug>', views.product_detail,name='product_detail'),
]
