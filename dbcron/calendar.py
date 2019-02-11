from datetime import date, timedelta, datetime
from calendar import HTMLCalendar
from dbcron import models


class JobCalendar(HTMLCalendar):
    table_class = "table"

    def __init__(self, jobs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jobs = jobs

    def get_table_class(self):
        return self.table_class

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table class="%s">' % (
            self.get_table_class()
        ))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def itermonthweekdays(self, theyear, themonth, theweek):
        for day_ in self.itermonthdates(theyear, themonth):
            if day_.isocalendar()[1] != theweek:
                continue
            yield day_

    def get_firstdateofweek(self, theyear, theweek):
        year_date = date(theyear, 1, 1)
        week_date = year_date + timedelta(days=theweek*7)
        first_day = week_date - timedelta(days=week_date.isocalendar()[1])
        return first_day

    def _format_jobs(self, v, first_day, dates):
        a = v.append
        day = first_day
        for i in range(7):
            a('<td>')
            a('<ul>')
            for job, jobtime in dates[day]:
                a('<li>')
                if hasattr(job, 'get_absolute_url'):
                    a('%s - <a href="%s">%s</a>' % (jobtime.strftime("%H:%M"), job.get_absolute_url(), job.name))
                else:
                    a('%s - %s' % (jobtime.strftime("%H:%M"), job.name))
                a('</li>')
            a('</ul>')
            a('</td>')
            a('\n')
            day += timedelta(days=1)

    def formatweekofmonth(self, theyear, theweek, withyear=True):
        v = []
        a = v.append
        a('<table class="%s">' % (
            self.get_table_class()
        ))
        # a('\n')
        # a(self.formatweekheader())
        a('\n')
        a('<tr>')
        a('<th></th>')
        for i in range(7):
            a('<th>%d</th>' % i)
        a('</tr>')
        day = self.get_firstdateofweek(theyear, theweek)
        dates = self.jobs.get_next_planned(
            from_=datetime(theyear, day.month, day.day-1, 23, 59),
            until=day+timedelta(days=7))
        a('<tr>')
        a('<td>')
        self._format_jobs(v, day, dates)
        a('</td>')
        a('<tr>')
        a('</table>')
        a('\n')
        return ''.join(v)
