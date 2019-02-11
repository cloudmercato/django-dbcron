from django.shortcuts import render
from django.utils.timezone import now
from django.utils.html import mark_safe
from dbcron import calendar


class JobCalendarMixin:
    calendar_class = calendar.JobCalendar

    def get_calendar_class(self):
        return self.calendar_class

    def get_calendar_kwargs(self):
        return {
            'jobs': self.object_list,
        }

    def get_calendar(self, calendar_class=None):
        klass = calendar_class or self.get_calendar_class()
        calendar_kwargs = self.get_calendar_kwargs()
        return klass(**calendar_kwargs)


class JobMonthCalendarMixin(JobCalendarMixin):
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        calendar = self.get_calendar()
        month_calendar = calendar.formatmonth(now().year, now().month)
        data.update({
            'calendar': calendar,
            'month_calendar': mark_safe(month_calendar),
        })
        return data


class JobWeekCalendarMixin(JobCalendarMixin):
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        calendar = self.get_calendar()
        week_calendar = calendar.formatweekofmonth(now().year, now().date().isocalendar()[1])
        data.update({
            'calendar': calendar,
            'week_calendar': mark_safe(week_calendar),
        })
        return data
