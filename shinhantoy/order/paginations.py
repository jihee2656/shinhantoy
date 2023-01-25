from rest_framework import pagination

class ProductListPagination(pagination.PageNumberPagination):
    page_size = 100000

