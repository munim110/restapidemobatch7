from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Book

class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author__name = CharFilter(field_name='author__name', lookup_expr='icontains')
    price = NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Book
        fields = ['title', 'price', 'author__name']