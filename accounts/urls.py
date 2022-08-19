from django.urls import path

from . import views


urlpatterns = [
    path('sing_up/', views.SingUpView.as_view(), name='singup'),
]
