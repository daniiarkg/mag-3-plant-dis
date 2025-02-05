from django.contrib import admin
from main.models import *


class ReportInline(admin.TabularInline):
    model = Report
    extra = 0
    # exclude = ['title','description']

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, **kwargs):
        print('FLAG 1111111   !!!!!!!!!!')
        return super().response_add(request, obj)
    def response_change(self, request, obj):
        print('FLAG!!!!!!!!!!')
        print(request)
        return super().response_change(request, obj)
    inlines = [
        ReportInline,
    ]

admin.site.register(Report)