from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view()),
    # path('companies/<int:pk>/', views.company_detail),
    path('cars/', views.CarList.as_view()),
    # path('cars/<int:pk>/', views.car_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)