# Generated by Django 2.2.1 on 2019-05-03 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190503_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_extra_data',
        ),
        migrations.CreateModel(
            name='CourseLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=100, verbose_name='链接名')),
                ('link_path', models.CharField(max_length=500, verbose_name='链接地址')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='课程号')),
            ],
            options={
                'verbose_name': '课程相关链接',
                'verbose_name_plural': '课程相关链接',
            },
        ),
    ]
