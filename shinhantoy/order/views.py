from django.shortcuts import render
from .paginations import ProductListPagination

# Create your views here.
class ProductListview():
    pagination_class = ProductListPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

