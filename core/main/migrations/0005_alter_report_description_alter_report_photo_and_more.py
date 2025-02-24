# Generated by Django 4.2.18 on 2025-02-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_plant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='photo',
            field=models.ImageField(null=True, upload_to='main'),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
