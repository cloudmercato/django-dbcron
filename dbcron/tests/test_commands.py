from unittest.mock import patch
from datetime import datetime
from concurrent import futures
from django.test import TestCase
from dbcron.management.commands.crond import Command
from dbcron.tests.factories import JobFactory


class CrondRunJobTest(TestCase):
    def setUp(self):
        self.command = Command()

    @patch('crontab.CronTab.next', return_value=42)
    def test_not_now(self, mock):
        job = JobFactory.create()
        result = self.command.run_job(job)
        self.assertIsNone(result)

    @patch('crontab.CronTab.next', return_value=0)
    def test_run(self, mock):
        job = JobFactory.create()
        result = self.command.run_job(job)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, datetime)

    @patch('crontab.CronTab.next', side_effect=Exception)
    def test_run_with_error(self, mock):
        job = JobFactory.create()
        with self.assertRaises(Exception):
            self.command.run_job(job)
