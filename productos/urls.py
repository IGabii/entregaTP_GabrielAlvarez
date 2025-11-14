from django.urls import path
from .views import ProductoListCreateView, ProductoRetrieveUpdateDestroyView

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-detail'),
]