from django.apps import AppConfig


class DbcronConfig(AppConfig):
    name = 'dbcron'
    label = 'dbcron'
    verbose_name = "Job scheduling"

    def ready(self):
        from dbcron import signals  # noqa
        from dbcron import consumers  # noqa
