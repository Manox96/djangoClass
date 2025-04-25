# Django Photo Gallery

Ce projet est une démonstration des concepts clés de Django: le routage, les vues et les templates.

## Structure du projet

### Routage (URLs)
Les routes sont définies dans:
- `myproject/urls.py` (URLs principal)
- `myapp/urls.py` (URLs de l'application)

Exemples de routes:
- Route simple: `path('', views.home, name='home')`
- Route avec paramètre: `path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail')`
- Route avec plusieurs paramètres: `path('category/<str:category_name>/photo/<int:photo_id>/', views.category_photo, name='category_photo')`
- Route pour vue basée sur classe: `path('photos/', views.PhotoListView.as_view(), name='photo_list')`

### Vues
Les vues sont définies dans `myapp/views.py`

Types de vues:
- **Vues basées sur fonctions**: `home()`, `contact()`, `photo_detail()`, etc.
- **Vues basées sur classes**:
  - `PhotoView` (classe de base `View`)
  - `AboutView` (classe `TemplateView`)
  - `PhotoListView` (classe `ListView`)
  - `PhotoDetailView` (classe `DetailView`)

### Templates
Les templates sont situés dans `myapp/templates/myapp/`

- `base.html` - template de base avec la structure HTML commune
- Templates spécifiques étendant le template de base
- Exemples de passage de données du contexte au template
- Exemple d'affichage de données de la base de données (`database_content.html`)

### Upload d'images
- Utilisation de `ImageField` dans le modèle `Photo`
- Configuration des fichiers média dans `settings.py`
- Formulaire d'upload avec enctype "multipart/form-data"
- Stockage des images uploadées dans le dossier `media/photos/`

## Installation

1. Cloner le projet
2. Installer les dépendances:
   ```
   pip install -r requirements.txt
   ```
3. Installer Pillow pour gérer les images:
   ```
   pip install Pillow
   ```  
4. Appliquer les migrations:
   ```
   python manage.py migrate
   ```
5. Créer un superutilisateur:
   ```
   python manage.py createsuperuser
   ```
6. Lancer le serveur:
   ```
   python manage.py runserver
   ```

## URLs disponibles

- `/` - Page d'accueil
- `/contact/` - Page de contact
- `/photo/<id>/` - Détail d'une photo (vue basée sur fonction)
- `/category/<nom>/<photo_id>/` - Photo dans une catégorie
- `/about/` - À propos (vue TemplateView)
- `/photos/` - Liste de photos (vue ListView)
- `/photos-detail/<id>/` - Détail d'une photo (vue DetailView)
- `/photo-view/<id>/` - Détail d'une photo (vue View)
- `/database/` - Affichage du contenu de la base de données
- `/upload/` - Formulaire d'upload de photos
- `/admin/` - Administration Django 