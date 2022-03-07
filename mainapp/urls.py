from django.urls import path

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile-view'),
]