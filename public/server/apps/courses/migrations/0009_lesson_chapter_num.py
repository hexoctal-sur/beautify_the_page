# Generated by Django 2.2.1 on 2019-05-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190503_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='chapter_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='章节数目'),
        ),
    ]
