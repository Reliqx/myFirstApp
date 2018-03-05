from django.urls import path, include
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    #login page
    path('login/', login, {'template_name': 'personal/login.html' }),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('user/profile/', views.profile, name='profile'),
    path('user/profile/edit/', views.edit_profile, name='edit_profile')
]
