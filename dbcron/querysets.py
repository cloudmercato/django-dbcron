from collections import defaultdict
from django.db import models


class JobQuerySet(models.QuerySet):
    def get_next_planned(self, until, from_=None):
        dates = defaultdict(list)
        for job in self.all():
            for next_date in job.get_next_planned(until, from_):
                dates[next_date.date()].append((job, next_date))
        for date in dates:
            dates[date] = sorted(dates[date], key=lambda x: x[1])
        return dates
