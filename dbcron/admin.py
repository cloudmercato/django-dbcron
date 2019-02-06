from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dbcron import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'func', 'is_active', 'next_time', 'sec', 'min', 'hou', 'dom',
                    'mon', 'dow', 'yea']
    list_filter = ['is_active', 'func']
    ordering = ['name']
    fieldsets = (
        (_('Metadata'), {
            'classes': ('wide',),
            'fields': (
                ('name', 'is_active'),
                'description',
            )
        }),
        (_("Operation"), {
            'classes': ('wide',),
            'fields': (
                'func',
                'opts',
            )
        }),
        (_("Scheduling"), {
            'classes': ('wide',),
            'fields': (
                ('sec', 'min', 'hou', 'dom', 'mon', 'dow', 'yea'),
            )
        }),
    )
