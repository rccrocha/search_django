from django.contrib.auth.models import User, Group
import django_filters
from django import forms

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='contains')	
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups']