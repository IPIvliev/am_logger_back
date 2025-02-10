from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from polygon import views

urlpatterns = [
    path('polygon/companies/<int:pk>', views.CompanyPolygonList.as_view()),
    path('polygon/user/company', views.UserCompanyPolygonCheck.as_view()),
    path('polygon/check_inn', views.CheckINN.as_view()),
    path('polygon/create_order', views.CreateOrder.as_view()),
    path('polygon/check_order', views.CheckOrder.as_view()),
    path('polygon/check_orders', views.CheckOrders.as_view()),
    path('polygon/get_events', views.GetEvents.as_view()),
    path('polygon/create_account', views.CreateAccount.as_view()),
    path('polygon/reset_password', views.ResetPassword.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)