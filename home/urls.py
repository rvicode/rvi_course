from django.urls import path

from . import views


app_name = 'home'
urlpatterns = [
    path('', views.LastUpdateView.as_view(), name='home'),
    path('all_video_update/', views.AllVideoUpdateView.as_view(), name='all_video_update'),
    path('all_video/', views.AllVideoView.as_view(), name='all_video'),
    path('detail/<int:pk>', views.video_detail_view, name='detail_video'),
    path('search/', views.search_view, name='search'),
    path('category_list/<int:pk>', views.category_list, name='category_list'),
    path('language_list/<int:pk>', views.language_list, name='language_list'),
    path('field_list/<int:pk>', views.field_list, name='field_list'),
    path('profile', views.about_us_view, name='about_us'),
]
