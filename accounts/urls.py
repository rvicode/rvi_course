from django.urls import path

from . import views


urlpatterns = [
    path('sing_up/', views.SingUpView.as_view(), name='singup'),
    path('panel/<int:pk>', views.UserPanelView.as_view(), name='user_panel'),
    path('edit_panel/', views.edit_user_panel_view, name='edit_user_panel'),
]
