from django import forms
import django_filters as filters
from dbcron import models


class JobFilterSet(filters.FilterSet):
    id = filters.BaseInFilter(widget=forms.HiddenInput)
    is_active = filters.BooleanFilter()

    class Meta:
        model = models.Job
        fields = []
