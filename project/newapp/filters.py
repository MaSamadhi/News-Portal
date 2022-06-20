import django_filters
from .models import Post
from django import forms


class PostFilter(django_filters.FilterSet):
    creationDate = django_filters.DateFilter(lookup_expr='gt',
                                             widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Post
        fields = {
            'postTitle': ['contains'],
            'postCategory': ['exact'],
            'categoryType': ['exact'],

        }