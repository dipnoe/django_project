from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from catalog.models import Category, Product, Blog


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': "It`s all in the DNA"
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


class CategoryView(ListView):
    model = Category


class ProductView(ListView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новый контакт!\n{name} ({phone}) написал: {message}\n')
    return render(request, 'catalog/contacts.html')


class BlogView(ListView):
    model = Blog
    fields = ['title', 'body', '']