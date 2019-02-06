# Generated by Django 2.0.8 on 2019-02-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='description')),
                ('func', models.CharField(max_length=250, verbose_name='function')),
                ('opts', models.TextField(default='{}', max_length=2000, verbose_name='options')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('sec', models.CharField(default='0', max_length=50, verbose_name='second(s)')),
                ('min', models.CharField(max_length=50, verbose_name='minute(s)')),
                ('hou', models.CharField(max_length=50, verbose_name='hour(s)')),
                ('dom', models.CharField(max_length=50, verbose_name='day(s) of month')),
                ('mon', models.CharField(max_length=50, verbose_name='month')),
                ('dow', models.CharField(max_length=50, verbose_name='day(s) of week')),
                ('yea', models.CharField(default='*', max_length=50, verbose_name='year(s)')),
            ],
            options={
                'verbose_name_plural': 'jobs',
                'verbose_name': 'job',
            },
        ),
    ]
