# Generated by Django 3.1.7 on 2021-07-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210725_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.CharField(max_length=100),
        ),
    ]
