from django.urls import path

from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeCoursesView.as_view(), name='home'),
    path('all_video/', views.AllVideoView.as_view(), name='all_video'),
    path('detail/<int:pk>', views.video_detail_view, name='detail_video'),
    path('search/', views.search_view, name='search')
]
