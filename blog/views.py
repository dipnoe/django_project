from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from pytils.translit import slugify
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body', 'is_published']
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body', 'is_published']

    def get_success_url(self):
        return reverse('blog:detail_blog', args=[self.object.pk])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')
