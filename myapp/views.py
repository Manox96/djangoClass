from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Photo
from .forms import PhotoUploadForm

# Home view with integrated upload form
@login_required(login_url='login')
def home(request):
    # Handle form submission
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploadée avec succès !')
            return redirect('home')
    else:
        form = PhotoUploadForm()
        
    # Get photos for display
    photos = Photo.objects.all().order_by('-upload_date')
    
    context = {
        'title': 'Accueil',
        'photos': photos,
        'form': form
    }
    return render(request, 'myapp/home.html', context)

# Photo list view
@login_required(login_url='login')
def photo_list(request):
    photos = Photo.objects.all().order_by('-upload_date')
    context = {
        'photos': photos
    }
    return render(request, 'myapp/photo_list.html', context)

# Photo detail view
@login_required(login_url='login')
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    photos = Photo.objects.all().order_by('-upload_date')
    context = {
        'photo': photo,
        'photos': photos,
    }
    return render(request, 'myapp/photo_detail.html', context)

# Class-based photo detail view
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'myapp/photo_detail.html'
    context_object_name = 'photo'

# Photo upload view
@login_required(login_url='login')
def upload_photo(request):
    photos = Photo.objects.all().order_by('-upload_date')
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploadée avec succès !')
            return redirect('photo_list')
    else:
        form = PhotoUploadForm()
    
    context = {
        'form': form,
        'photos': photos,
    }
    return render(request, 'myapp/upload_photo.html', context)

@login_required(login_url='login')
def toggle_favorite(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user in photo.favorites.all():
        photo.favorites.remove(request.user)
    else:
        photo.favorites.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'photo_list'))

def login_view(request):
    # If user is already logged in, redirect to photo list
    if request.user.is_authenticated:
        return redirect('photo_list')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            # Get the next parameter from the URL, default to photo_list
            next_url = request.GET.get('next', 'photo_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'myapp/login.html')

def register_view(request):
    # If user is already logged in, redirect to photo list
    if request.user.is_authenticated:
        return redirect('photo_list')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'myapp/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'myapp/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'myapp/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('photo_list')
    
    return render(request, 'myapp/register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 