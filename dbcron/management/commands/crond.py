import time
import logging
from concurrent import futures

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from dbcron import models
from dbcron import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    @property
    def logger(self):
        if not hasattr(self, '_logger'):
            self._logger = logging.getLogger('dbcron')
        return self._logger

    def run_job(self, job):
        next_ = int(job.entry.next())
        if next_ != 0:
            self.logger.debug("%s will run in %ssec", job.name, next_)
            return
        self.logger.info("started %s", job.name)
        try:
            result = job.run()
        except Exception as err:
            self.logger.exception("error with %s", job.name)
            raise
        finally:
            self.logger.info("finished %s", job.name)
        return result

    def main(self, executor):
        jobs = models.Job.objects.filter(is_active=True)
        self.stdout.write(self.style.SUCCESS('Started'))
        while True:
            self.logger.debug("new loop")
            executor.map(self.run_job, jobs.all())
            time.sleep(1)

    def handle(self, *args, **options):
        executor = futures.ThreadPoolExecutor(max_workers=settings.MAX_WORKERS)
        try:
            self.main(executor)
        except KeyboardInterrupt as err:
            executor.shutdown()
            self.stdout.write(self.style.WARNING('Stopped'))
            return
