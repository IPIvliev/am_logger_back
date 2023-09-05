from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from labor import views

urlpatterns = [
    path('protection/', views.ReportList.as_view()),
    path('protection/<int:pk>/', views.ChecklistList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)