from django.contrib import admin
from .models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_at', )
    list_display = ('id' ,'status', 'created_at', 'image_tag')
    readonly_fields = ('kp_number', 'large_image_tag', 'phone')

