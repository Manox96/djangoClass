from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Photo
from .forms import PhotoUploadForm

# Home view with integrated upload form
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

# Photo detail view
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    context = {
        'photo': photo
    }
    return render(request, 'myapp/photo_detail.html', context) 