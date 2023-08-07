from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
app_name = BlogConfig.name

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog')
]
