# Generated by Django 3.2.8 on 2021-12-01 18:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 405789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empowerment',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 437039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 437039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='legislative_activitie',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 421418, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 405789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 18, 32, 58, 437039, tzinfo=utc)),
        ),
    ]
