from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from .models import Title


class TitleFilter(FilterSet):
    """Фильтрация произведений по имени, году"""
    name = CharFilter(field_name='name', lookup_expr='icontains')
    year = NumberFilter()

    class Meta:
        model = Title
        fields = ['name', 'year']
