from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


def products_add_view(request):
    if request.method == 'GET':
        context = {'categories': Category.objects.all()}
        return render(request, 'product_add.html', context=context)
    product_data = {
        'name': request.POST.get('name'),
        'category': get_object_or_404(Category, title=request.POST.get('title')),
        'description': request.POST.get('description', None),
        'price': request.POST.get('price'),
        'image': request.POST.get('image')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)


def products_delete_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('products_view')


def products_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        context = {
            'product': product,
            'categories': Category.objects.all()
        }
        return render(request, 'product_edit.html', context=context)
    product.name = request.POST.get('name')
    product.category = get_object_or_404(Category, title=request.POST.get('title'))
    product.description = request.POST.get('description', None)
    product.price = request.POST.get('price')
    product.image = request.POST.get('image')
    product.save()
    return redirect('products_view')
