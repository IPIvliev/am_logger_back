from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from detection import views

urlpatterns = [
    path('cars_detection/', views.RecognitionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)