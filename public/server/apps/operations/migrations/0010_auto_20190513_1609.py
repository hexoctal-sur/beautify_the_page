# Generated by Django 2.2.1 on 2019-05-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0009_auto_20190503_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproblem',
            name='problem_img',
            field=models.TextField(blank=True, null=True, verbose_name='问题图片'),
        ),
    ]
