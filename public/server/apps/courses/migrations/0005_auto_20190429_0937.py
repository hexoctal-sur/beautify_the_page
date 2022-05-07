# Generated by Django 2.2 on 2019-04-29 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190424_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_img',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='课程封面'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 9, 37, 31, 843965), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 9, 37, 31, 843965), verbose_name='发布时间'),
        ),
    ]
