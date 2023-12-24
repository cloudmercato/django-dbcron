from django import forms
from dbcron import models


class AbstractJobForm:
    sec = forms.CharField(
        initial='0',
        label="Second(s)"
    )
    min = forms.CharField(
        initial='*',
        label="Minute(s)"
    )
    hou = forms.CharField(
        initial='*',
        label="Hour(s)"
    )
    dom = forms.CharField(
        initial='*',
        label="Day(s) of month"
    )
    mon = forms.CharField(
        initial='*',
        label="Month"
    )
    dow = forms.CharField(
        initial='*',
        label="Day(s) of week"
    )
    yea = forms.CharField(
        initial='*',
        label="Year(s)"
    )


class JobForm(AbstractJobForm, forms.ModelForm):
    class Meta:
        model = models.Job
        fields = '__all__'
