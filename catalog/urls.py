from django.urls import path

from catalog.views import (HomeView, contacts, ProductView, CategoryView, BlogView, BlogCreateView,
                           BlogUpdateView, BlogDeleteView, BlogDetailView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryView.as_view(), name='category'),
    path('<int:pk>/product/', ProductView.as_view(), name='product'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/create', BlogCreateView.as_view(), name='create_blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog')
]
