from django.urls import path
from . import views

app_name = 'calc'
urlpatterns = [
    path('', views.index, name="index"),
    path('description/', views.description, name="description"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]