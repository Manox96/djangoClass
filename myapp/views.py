from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from .models import Photo
from .forms import PhotoUploadForm

# Create your views here.

# Function-based view example
def home(request):
    
    photos = Photo.objects.filter(is_pulic=True).order_by('-upload_date')
    context = {
        'title': 'Accueil',
        'photos': photos
    }
    return render(request, 'myapp/home.html', context)

# Another function-based view example
def contact(request):
    
    context = {
        'title': 'Contact',
        'email': 'contact@example.com',
        'address': '123 Main Street, City'
    }
    return render(request, 'myapp/contact.html', context)

# Function-based view with parameter
def photo_detail(request, photo_id):
    
    photo = get_object_or_404(Photo, id=photo_id)
    context = {
        'photo': photo
    }
    return render(request, 'myapp/photo_detail.html', context)

# Function-based view with multiple parameters
def category_photo(request, category_name, photo_id):
    
    photo = get_object_or_404(Photo, id=photo_id)
    context = {
        'category': category_name,
        'photo': photo
    }
    return render(request, 'myapp/category_photo.html', context)

# Class-based view example
class PhotoView(View):
    
    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        return render(request, 'myapp/photo_view.html', {'photo': photo})

# TemplateView example
class AboutView(TemplateView):
    
    template_name = 'myapp/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['description'] = 'We are a photo sharing platform.'
        return context

# ListView example
class PhotoListView(ListView):
    
    model = Photo
    template_name = 'myapp/photo_list.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        return Photo.objects.filter(is_pulic=True).order_by('-upload_date')

# DetailView example
class PhotoDetailView(DetailView):
    
    model = Photo
    template_name = 'myapp/photo_detail_class.html'
    context_object_name = 'photo'

# View to display database content
def database_content(request):
    
    photos = Photo.objects.all().order_by('-upload_date')
    context = {
        'photos': photos
    }
    return render(request, 'myapp/database_content.html', context)

# View for uploading photos
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploadée avec succès !')
            return redirect('photo_list')
    else:
        form = PhotoUploadForm()
    
    return render(request, 'myapp/upload_photo.html', {'form': form})
