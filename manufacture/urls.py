from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from manufacture import views

urlpatterns = [
    path('equipments/', views.EquipmentList.as_view()),
    path('equipment/<int:pk>/parameters/', views.ParameterList.as_view()),
    path('equipment/parameters/', views.AllParameterList.as_view()),
    path('equipment/parameters/last/', views.LastParameterList.as_view()),
    path('equipment/<int:pk>/parameters/add', views.ParameterAdd.as_view()),
    path('stopreports/', views.StopReportList.as_view()),
    path('production/', views.ProductionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)