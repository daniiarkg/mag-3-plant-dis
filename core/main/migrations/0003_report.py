# Generated by Django 4.2.18 on 2025-02-05 08:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_plant_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to='main')),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.plant')),
            ],
        ),
    ]
