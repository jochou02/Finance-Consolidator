from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chart, name='chart'),
    path('update_transaction/<str:pk>/', views.updateTransaction, name='update_transaction')
]