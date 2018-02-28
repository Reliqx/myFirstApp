from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('registration_form/', views.UserFormView.as_view(), name='register'),
]
