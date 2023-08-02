from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': "It`s all in the DNA"
    }
    return render(request, 'catalog/home.html', context)


def category(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'catalog/category.html', context)


def product(request, pk):
    context = {
        'object_list': Product.objects.filter(category=pk)
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новый контакт!\n{name} ({phone}) написал: {message}\n')
    return render(request, 'catalog/contacts.html')
