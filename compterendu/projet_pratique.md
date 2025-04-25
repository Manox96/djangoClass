# Projet Pratique : Système de gestion de bibliothèque

Ce projet vous guide à travers la création d'un système de gestion de bibliothèque en utilisant Django, en mettant l'accent sur les modèles et les migrations.

## Étape 1 : Configuration du projet

```bash
# Créer un nouvel environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer Django
pip install django

# Créer un nouveau projet
django-admin startproject bibliotheque

# Créer une application
cd bibliotheque
python manage.py startapp livres
```

## Étape 2 : Définir les modèles

Créez les modèles suivants dans `livres/models.py` :

```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    biographie = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ['nom', 'prenom']

class Genre(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    resume = models.TextField(blank=True)
    date_publication = models.DateField()
    nombre_pages = models.PositiveIntegerField(default=0)
    
    # Relations
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')
    genres = models.ManyToManyField(Genre, related_name='livres')
    
    # Statut du livre
    STATUT_CHOICES = [
        ('D', 'Disponible'),
        ('P', 'Prêté'),
        ('R', 'Réservé'),
        ('M', 'Maintenance'),
    ]
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES, default='D')
    
    def __str__(self):
        return self.titre

class Emprunt(models.Model):
    # Relations
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT, related_name='emprunts')
    emprunteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprunts')
    
    # Dates
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True, blank=True)
    
    def est_en_retard(self):
        if not self.date_retour_effective and timezone.now().date() > self.date_retour_prevue:
            return True
        return False
    
    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.emprunteur.username}"
```

## Étape 3 : Enregistrer l'application dans settings.py

Modifiez `bibliotheque/settings.py` pour ajouter votre application :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livres',  # Ajout de notre application
]
```

## Étape 4 : Créer et appliquer les migrations

```bash
# Générer les migrations
python manage.py makemigrations livres

# Vérifier le SQL généré (optionnel)
python manage.py sqlmigrate livres 0001

# Appliquer les migrations
python manage.py migrate
```

## Étape 5 : Enregistrer les modèles dans l'admin

Créez ou modifiez `livres/admin.py` :

```python
from django.contrib import admin
from .models import Auteur, Genre, Livre, Emprunt

class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'statut', 'isbn')
    list_filter = ('statut', 'date_publication')
    search_fields = ('titre', 'isbn', 'auteur__nom')

class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('livre', 'emprunteur', 'date_emprunt', 'date_retour_prevue', 'est_en_retard')
    list_filter = ('date_emprunt', 'date_retour_prevue')
    search_fields = ('livre__titre', 'emprunteur__username')

admin.site.register(Auteur)
admin.site.register(Genre)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Emprunt, EmpruntAdmin)
```

## Étape 6 : Migration - Ajout d'un nouveau champ

Maintenant, modifiez votre modèle pour ajouter un nouveau champ :

```python
# Dans livres/models.py, ajoutez ce champ au modèle Livre
edition = models.CharField(max_length=100, blank=True)
```

Puis créez et appliquez une nouvelle migration :

```bash
python manage.py makemigrations livres
python manage.py migrate
```

## Étape 7 : Migration avec données personnalisées

Créez une migration vide pour ajouter des données initiales :

```bash
python manage.py makemigrations --empty livres --name=ajouter_genres_courants
```

Puis modifiez le fichier de migration créé (dans `livres/migrations/`) :

```python
from django.db import migrations

def ajouter_genres(apps, schema_editor):
    # Nous récupérons le modèle via apps pour éviter les problèmes de versionnement
    Genre = apps.get_model('livres', 'Genre')
    
    # Création des genres
    genres = [
        {"nom": "Roman", "description": "Œuvre littéraire en prose."},
        {"nom": "Science-Fiction", "description": "Genre narratif présentant des univers où les avancées technologiques et scientifiques sont extrapolées."},
        {"nom": "Fantastique", "description": "Genre où le cadre narratif intègre des éléments surnaturels."},
        {"nom": "Policier", "description": "Roman ayant pour thème principal l'élucidation d'un mystère, le plus souvent criminel."},
        {"nom": "Biographie", "description": "Récit retraçant la vie d'une personne."},
    ]
    
    for genre_data in genres:
        Genre.objects.create(**genre_data)

def supprimer_genres(apps, schema_editor):
    Genre = apps.get_model('livres', 'Genre')
    Genre.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('livres', '0002_livre_edition'),  # Assurez-vous de mettre la bonne dépendance
    ]
    
    operations = [
        migrations.RunPython(ajouter_genres, supprimer_genres),
    ]
```

Appliquez cette migration :

```bash
python manage.py migrate
```

## Étape 8 : Requêtes depuis la console Django

Pour tester vos modèles, vous pouvez utiliser la console Django :

```bash
python manage.py shell
```

```python
# Importer les modèles
from livres.models import Auteur, Genre, Livre, Emprunt
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Créer un auteur
auteur = Auteur.objects.create(
    nom="Dumas",
    prenom="Alexandre",
    date_naissance="1802-07-24"
)

# Récupérer un genre
genre_roman = Genre.objects.get(nom="Roman")

# Créer un livre
livre = Livre.objects.create(
    titre="Le Comte de Monte-Cristo",
    isbn="9782080703859",
    resume="Edmond Dantès, injustement emprisonné, s'évade et entreprend sa vengeance...",
    date_publication="1844-01-01",
    nombre_pages=1312,
    auteur=auteur
)

# Ajouter des genres au livre
livre.genres.add(genre_roman)
livre.save()

# Créer un utilisateur (pour les emprunts)
user = User.objects.create_user('jean', 'jean@example.com', 'motdepasse')

# Créer un emprunt
date_retour = timezone.now().date() + datetime.timedelta(days=14)
emprunt = Emprunt.objects.create(
    livre=livre,
    emprunteur=user,
    date_retour_prevue=date_retour
)

# Marquer le livre comme prêté
livre.statut = 'P'
livre.save()

# Faire des requêtes
print("Tous les livres de l'auteur:", auteur.livres.all())
print("Tous les livres du genre roman:", Genre.objects.get(nom="Roman").livres.all())
print("Livres disponibles:", Livre.objects.filter(statut='D'))
print("Emprunts en cours:", Emprunt.objects.filter(date_retour_effective=None))
```

## Prochaines étapes

1. Créez des vues et des templates pour afficher les livres et gérer les emprunts
2. Implémentez un système de recherche
3. Ajoutez une authentification utilisateur
4. Configurez des permissions (qui peut emprunter, qui peut gérer l'inventaire)
5. Ajoutez des validations personnalisées (par exemple, limiter le nombre d'emprunts par utilisateur) 