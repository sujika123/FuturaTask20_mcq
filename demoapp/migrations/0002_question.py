# Generated by Django 4.2.2 on 2023-12-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100, null=True)),
                ('Ans', models.CharField(max_length=100)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('checkans', models.BooleanField(default=False)),
                ('time', models.TimeField()),
            ],
        ),
    ]
