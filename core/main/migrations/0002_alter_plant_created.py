# Generated by Django 4.2.18 on 2025-02-05 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
