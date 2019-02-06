from datetime import timedelta
from django.contrib import admin
from django.template.defaultfilters import timeuntil
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from dbcron import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'func', 'is_active', 'next_time', 'sec', 'min', 'hou', 'dom',
                    'mon', 'dow', 'yea']
    list_filter = ['is_active', 'func']
    actions = ('make_disable', 'make_enable')
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
    
    def next_time(self, obj):
        next_ = obj.next_time
        if next_ is None:
            return '-'
        dst_date = now() + timedelta(seconds=next_)
        return timeuntil(dst_date)
    next_time.short_description = _("Next run")
    
    def make_disable(self, request, queryset):
        queryset.update(is_active=False)
    make_disable.short_description = _("Disable job(s)")

    def make_enable(self, request, queryset):
        queryset.update(is_active=True)
    make_enable.short_description = _("Enable job(s)")
