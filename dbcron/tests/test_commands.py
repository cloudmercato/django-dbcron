from unittest.mock import patch
from datetime import datetime

from django.test import TestCase
from django.core.management import call_command

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


class CrondCommandTest(TestCase):
    @patch('dbcron.management.commands.crond.Command.stop', side_effect=(False, True))
    def test_run(self, mock):
        call_command('crond')
        self.assertEqual(mock.call_count, 2)

    @patch('dbcron.management.commands.crond.Command.run_job', return_value=True)
    @patch('dbcron.management.commands.crond.Command.stop', return_value=True)
    def test_filter_tags(self, mock_stop, mock_run_job):
        JobFactory.create(tag='foo')
        call_command('crond', '--tags', 'foo')
        self.assertEqual(mock_run_job.call_count, 1)

    @patch('dbcron.management.commands.crond.Command.run_job', return_value=True)
    @patch('dbcron.management.commands.crond.Command.stop', return_value=True)
    def test_filter_tags(self, mock_stop, mock_run_job):
        JobFactory.create(tag='foo')
        call_command('crond', '--tags', 'bar')
        self.assertEqual(mock_run_job.call_count, 0)
