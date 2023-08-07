from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, ProductView, CategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryView.as_view(), name='category'),
    path('<int:pk>/product/', ProductView.as_view(), name='product')
]
