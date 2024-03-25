from django.db import models
from django.utils.html import mark_safe
import requests
from django.http import request

STATUS_CHOICES = (
    ('N', 'Новое'),
    ('W', 'В работе'),
    ('C', 'Закрыто'),
)

class BotUser(models.Model):
    name = models.CharField('Ник пользователя', max_length=150, null=True, blank=True)
    uid = models.CharField('Chat ID пользователя', max_length=30, null=False, blank=False)
    bot_name = models.CharField('Бот', max_length=30, null=False, blank=False)
    active = models.BooleanField('Активен', default = True)

    class Meta:
        verbose_name='Пользователь телеграм бота'
        verbose_name_plural='Пользователи телеграм бота'

    def save(self, *args, **kwargs):
        return super(BotUser, self).save(*args, **kwargs)

class Appeal(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='N')
    comment = models.TextField('Комментарий', null=True, blank=True)
    kp_number = models.CharField('Номер контейнерной площадки', max_length=50, null=False, blank=False)
    phone = models.CharField('Номер телефона заявителя', max_length=15, null=True, blank=True)
    image = models.ImageField('Фотография', upload_to='appeals/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Обращение гражданина'
        verbose_name_plural='Обращения граждан'

    def image_tag(self):
        return mark_safe('<img src="/public_html/media/%s" width="150" />' % (self.image))

    image_tag.short_description = 'Обзорное фото'

    def large_image_tag(self):
        return mark_safe('<img src="/public_html/media/%s" width="480" />' % (self.image))

    large_image_tag.short_description = 'Обзорное фото'

    def save(self, *args, **kwargs):
        if self.comment:
            msg = "Мы получили новую жалобу на вывоз мусора!\n<b>Текст комментария:</b>\n" + str(self.comment)
        else:
            msg = "Мы получили новую жалобу на вывоз мусора!"
        
        borusers = BotUser.objects.filter(active = True)

        super(Appeal, self).save(*args, **kwargs)

        if self.image:
            for botuser in borusers: 
                requests.get(
                    'https://api.telegram.org/bot6933817234:AAG96yqdcxr5140SKrxVAal97VBh6Z189hs/sendPhoto',
                    params={'chat_id': botuser.uid, 'photo': 'https://amlogger-back.mag-rf.ru'+self.image.url, 'caption': msg, 'parse_mode': 'HTML'},
                )  
        else:
            for botuser in borusers: 
                requests.get(
                    'https://api.telegram.org/bot6933817234:AAG96yqdcxr5140SKrxVAal97VBh6Z189hs/sendMessage',
                    params={'chat_id': botuser.uid, 'text': msg, 'parse_mode': 'HTML'},
                )

        