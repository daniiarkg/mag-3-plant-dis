from django.db import models
from django.utils.timezone import now
import main.pred as pr
from pathlib import Path
from django.db.models.signals import post_save

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(default=now)


class Report(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='main', null=True)

def change_text(id):
    instance = Report.objects.get(pk=id)
    pred = pr.prediction( str(BASE_DIR) + instance.photo.url)
    instance.title = pr.disease_info['disease_name'][pred]
    instance.description = pr.disease_info['description'][pred]
    instance.save()

def report_loaded(sender, instance, created, **kwargs):
    if created:
        change_text(instance.pk)

post_save.connect(report_loaded, sender=Report)