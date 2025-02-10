from django.contrib import admin
from .models import CompanyPolygon

@admin.register(CompanyPolygon)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'director')