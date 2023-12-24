from django.contrib import admin
from dbcron import models
from dbcron import utils


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag', 'func', 'is_active', 'next_time', 'sec',
                    'min', 'hou', 'dom', 'mon', 'dow', 'yea']
    list_filter = ['is_active', 'func', 'tag']
    actions = ('make_disable', 'make_enable')
    ordering = ['name']
    fieldsets = (
        ('Metadata', {
            'classes': ('wide',),
            'fields': (
                ('name', 'tag', 'is_active'),
                'description',
            )
        }),
        ("Operation", {
            'classes': ('wide',),
            'fields': (
                'func',
                'args',
                'opts',
            )
        }),
        ("Scheduling", {
            'classes': ('wide',),
            'fields': (
                ('sec', 'min', 'hou', 'dom', 'mon', 'dow', 'yea'),
            )
        }),
    )

    def next_time(self, obj):
        return utils.get_next_time(obj) or '-'
    next_time.short_description = "Next run"

    def make_disable(self, request, queryset):
        queryset.update(is_active=False)
    make_disable.short_description = "Disable job(s)"

    def make_enable(self, request, queryset):
        queryset.update(is_active=True)
    make_enable.short_description = "Enable job(s)"
