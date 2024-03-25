from django.contrib import admin
from .models import Appeal, BotUser


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_at', )
    list_display = ('id' ,'status', 'created_at', 'image_tag')
    readonly_fields = ('kp_number', 'large_image_tag', 'phone', 'created_at')

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_filter = ('bot_name', )
    list_display = ('id' ,'name', 'uid', 'bot_name', 'active')
    readonly_fields = ('name', 'uid', 'bot_name')

