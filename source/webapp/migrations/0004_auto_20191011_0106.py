# Generated by Django 2.2 on 2019-10-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191011_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Project name'),
        ),
    ]