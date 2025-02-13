from django.contrib import admin
from .models import Equipment, Parameter, StopReport, Production


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'created_at')

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_filter = ('equipment', 'created_at')
    list_display = ('id' ,'equipment', 'name', 'value', 'created_at')
    # readonly_fields = ('equipment', 'created_at', )

@admin.register(StopReport)
class StopReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'finished_at', 'stop_period', 'status')

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_filter = ('product', 'created_at')
    list_display = ('batch', 'product', 'weight', 'created_at')