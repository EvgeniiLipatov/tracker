# Generated by Django 2.2 on 2019-12-05 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_project_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='task',
        ),
    ]