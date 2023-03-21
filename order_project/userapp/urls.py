from django.urls import path

from . import views

app_name = 'userapp'

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]