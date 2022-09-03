from django.urls import path

from . import views


app_name = 'home'
urlpatterns = [
    path('', views.ListUpdateView.as_view(), name='home'),
    path('all_video_update/', views.AllVideoUpdateView.as_view(), name='all_video_update'),
    path('all_video/', views.AllVideoView.as_view(), name='all_video'),
    path('detail/<int:pk>', views.video_detail_view, name='detail_video'),
    path('search/', views.search_view, name='search'),
    path('category_list/<int:pk>', views.category_list, name='category_list'),
    path('language_list/<int:pk>', views.language_list, name='language_list'),
    path('field_list/<int:pk>', views.field_list, name='field_list'),
    path('profile', views.about_us_view, name='about_us'),
    path('contact_us', views.contact_us_view, name='contact_us'),
    path('create_video', views.CreateVideoView.as_view(), name='create_video'),
    path('update_video/<int:pk>', views.UpdateVideoView.as_view(), name='update_video'),
    path('delete_video/<int:pk>', views.DeleteVideoView.as_view(), name='delete_video'),
]
