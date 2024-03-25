from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appeal import views

urlpatterns = [
    path('appeals/', views.AppealList.as_view()),
    path('botusers/', views.BotUserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)