# Generated by Django 2.2.1 on 2019-05-02 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190427_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 9, 48, 23, 497667)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.CharField(blank=True, max_length=11300, null=True, verbose_name='头像'),
        ),
    ]
