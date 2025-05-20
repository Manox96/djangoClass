from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.login_view, name='login'),  # Make login the default landing page
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin URLs - Changed from 'admin/' to 'dashboard/'
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/user/<int:user_id>/edit/', views.admin_edit_user, name='admin_edit_user'),
    path('dashboard/user/<int:user_id>/delete/', views.admin_delete_user, name='admin_delete_user'),
    
    # Main views
    path('home/', views.home, name='home'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('photo/class/<int:photo_id>/', views.PhotoDetailView.as_view(), name='photo_detail_class'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('photo/<int:photo_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_photos, name='favorite_photos'),
    path('photo/<int:photo_id>/update/', views.update_photo, name='update_photo'),
] 