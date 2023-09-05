from django.contrib import admin
from .models import Car, Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_cars')


    @admin.display(description='Кол-во машин')
    def get_cars(self, obj):
        return [len(obj.cars.all())]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_filter = ('company',)
    list_display = ('number', 'company')
