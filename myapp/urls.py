from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('category/<str:category_name>/photo/<int:photo_id>/', views.category_photo, name='category_photo'),
    
    
    path('photo-view/<int:photo_id>/', views.PhotoView.as_view(), name='photo_view'),
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('photos-detail/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail_class'),
    
    path('database/', views.database_content, name='database_content'),
    
    path('upload/', views.upload_photo, name='upload_photo'),
] 