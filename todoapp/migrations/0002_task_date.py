# Generated by Django 4.2.5 on 2023-09-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-02-05'),
            preserve_default=False,
        ),
    ]
