"""
Exemples de modèles Django basiques
"""
from django.db import models
from django.utils import timezone


class Livre(models.Model):
    """
    Modèle représentant un livre dans une bibliothèque.
    """
    # Champs texte
    titre = models.CharField(max_length=200, help_text="Titre du livre")
    auteur = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    # Champs numériques
    nombre_pages = models.IntegerField(default=0)
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    # Champs date
    date_publication = models.DateField()
    date_ajout = models.DateTimeField(default=timezone.now)
    
    # Champ booléen
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        """Représentation textuelle du modèle"""
        return self.titre
    
    class Meta:
        """Meta options"""
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        ordering = ['-date_ajout']  # Tri par date d'ajout décroissante


class Utilisateur(models.Model):
    """
    Modèle représentant un utilisateur de la bibliothèque.
    """
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    
    STATUT_CHOICES = [
        ('A', 'Actif'),
        ('I', 'Inactif'),
        ('B', 'Bloqué'),
    ]
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES, default='A')
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        
        
# Comment enregistrer un modèle dans l'admin Django:
"""
Dans admin.py:

from django.contrib import admin
from .models import Livre, Utilisateur

admin.site.register(Livre)
admin.site.register(Utilisateur)
""" 