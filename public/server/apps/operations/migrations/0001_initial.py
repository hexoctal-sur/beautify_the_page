# Generated by Django 2.2 on 2019-04-24 02:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20190424_1025'),
        ('users', '0002_auto_20190424_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notebook_content', models.TextField(blank=True, null=True, verbose_name='笔记内容')),
                ('notebook_date', models.DateTimeField(default=datetime.datetime(2019, 4, 24, 10, 25, 44, 684517), verbose_name='发布时间')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='课程号')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户号')),
            ],
            options={
                'verbose_name': '用户笔记',
                'verbose_name_plural': '用户笔记',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=50, verbose_name='消息标题')),
                ('message_content', models.CharField(max_length=500, verbose_name='消息内容')),
                ('message_date', models.DateTimeField(default=datetime.datetime(2019, 4, 24, 10, 25, 44, 683516), verbose_name='发送时间')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户号')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
                'ordering': ('user_id', 'message_date'),
            },
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateTimeField(default=datetime.datetime(2019, 4, 24, 10, 25, 44, 683516), verbose_name='浏览时间')),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter', verbose_name='章节号')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='课程号')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户号')),
            ],
            options={
                'verbose_name': '浏览历史',
                'verbose_name_plural': '浏览历史',
                'ordering': ('user_id', 'history_date'),
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=500, verbose_name='评论内容')),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2019, 4, 24, 10, 25, 44, 684517), verbose_name='发布时间')),
                ('comment_agree', models.IntegerField(default=0, verbose_name='点赞数')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户号')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
    ]