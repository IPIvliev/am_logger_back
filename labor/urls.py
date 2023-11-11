from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from labor import views

urlpatterns = [
    path('protection/', views.ReportList.as_view()),
    path('protection/<int:pk>/', views.ChecklistList.as_view()),
    path('protection/<int:pk>/destroy', views.ChecklistDestroy.as_view()),
    path('answer/<int:pk>/update', views.AnswerUpdate.as_view()),
    path('checklist/<int:pk>/update', views.ChecklistUpdate.as_view()),
    path('checklists/', views.ChecklistAll.as_view()),
    path('checklistscount/', views.ChecklistCount.as_view()),
    path('statistic/', views.StatisticCount.as_view()),
    path('get_video', views.GetVideo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)