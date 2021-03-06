# Generated by Django 3.2.8 on 2021-12-01 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polweb', '0007_auto_20211201_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img3',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 114996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empowerment',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 130611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 130611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='legislative_activitie',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 114996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 99360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 1, 19, 43, 50, 130611, tzinfo=utc)),
        ),
    ]
