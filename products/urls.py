from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("",views.product_list,name="product-list"),
    path("product/<int:id>/",views.product_detail,name="product-detail"),
    path("product/create/",views.product_create,name="product-create"),
    path("product/<int:id>/update/",views.product_update,name="product-update"),
    path("product/<int:id>/delete/",views.product_delete,name="product-delete"),
]