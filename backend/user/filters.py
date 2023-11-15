from django.db.models import Q
from django_filters import rest_framework as filters

from .models import User


class UserFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id")
    role = filters.CharFilter(field_name="role")
    search = filters.CharFilter(method="search_filter")

    class Meta:
        model = User
        fields = ["id", "role"]

    def search_filter(self, queryset, name, value):
        return queryset.filter_search(value)
