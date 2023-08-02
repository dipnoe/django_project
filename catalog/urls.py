from django.urls import path

from catalog.views import home, contacts, product, category

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/product/', product, name='product'),
]
