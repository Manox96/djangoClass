from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.login_view, name='login'),  # Make login the default landing page
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Main views
    path('home/', views.home, name='home'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('photo/class/<int:photo_id>/', views.PhotoDetailView.as_view(), name='photo_detail_class'),
    path('upload/', views.upload_photo, name='upload_photo'),
] 