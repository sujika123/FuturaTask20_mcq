# Generated by Django 4.2.2 on 2023-12-02 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
    ]