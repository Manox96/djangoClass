from django.urls import path
from . import views

urlpatterns = [
    # Main views
    path('', views.home, name='home'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
] 