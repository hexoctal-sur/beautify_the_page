# Generated by Django 2.2 on 2019-04-29 15:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0005_auto_20190429_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 15, 9, 40, 626901), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.UserProblem', verbose_name='评论问题'),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='history_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 15, 9, 40, 626901), verbose_name='浏览时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 15, 9, 40, 626901), verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='usernotebook',
            name='notebook_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 15, 9, 40, 626901), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='userproblem',
            name='problem_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 15, 9, 40, 626901), verbose_name='发布时间'),
        ),
    ]
