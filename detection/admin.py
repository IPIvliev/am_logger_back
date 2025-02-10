from django.contrib import admin
from detection.models import Camera, DetectionSettings, Recognition
from django.db.utils import ProgrammingError
from django.utils.html import format_html

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'created_at', 'status')

@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    def plate_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.plate_image.url))
    
    def car_tag(self, obj):
        return format_html('<img src="{}" style="max-width:640px; max-height:400px"/>'.format(obj.car_image.url))

    list_display = ['id', 'source', 'plate_text', 'plate_tag', 'ratio', 'created_at']
    readonly_fields = ('ratio', 'plate_text', 'plate_tag', 'car_tag', 'source', 'created_at')
    fields = ('ratio', 'plate_text', 'source', 'plate_tag', 'car_tag', 'created_at')

@admin.register(DetectionSettings)
class DetectionSettingsAdmin(admin.ModelAdmin):
    class Meta:
        name = "Настройки детекции"

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

        try:
            DetectionSettings.load().save()
        except ProgrammingError:
            pass
 
    def has_add_permission(self, request, obj=None):
        return False
 
    def has_delete_permission(self, request, obj=None):
        return False