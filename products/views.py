from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render( request, "products/detail.html", {"product": product} )


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products:product-list")
    else:
        form = ProductForm()
    return render(request, "products/create.html", {"form": form})

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect(
                "products:product-detail",
                id=product.id
            )
    else:
        form = ProductForm(instance=product)
    return render(request, "products/update.html", {"form": form, "product": product})


def product_delete(request, id):

    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("products:product-list")

    return render(request, "products/delete.html", {"product": product})