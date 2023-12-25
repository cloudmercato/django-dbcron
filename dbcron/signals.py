from django.dispatch import Signal

job_started = Signal()
job_done = Signal()
job_failed = Signal()
