"""
Exemples avancés de modèles Django avec différents types de relations
"""
from django.db import models
from django.utils import timezone
import uuid


class Auteur(models.Model):
    """
    Modèle représentant un auteur de livres
    """
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    biographie = models.TextField(blank=True)
    photo = models.ImageField(upload_to='auteurs/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        ordering = ['nom', 'prenom']


class Categorie(models.Model):
    """
    Modèle représentant une catégorie de livres
    """
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Livre(models.Model):
    """
    Modèle représentant un livre avec relations
    """
    # Identifiant UUID au lieu d'entier auto-incrémenté
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Champs basiques
    titre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    resume = models.TextField(blank=True)
    nombre_pages = models.PositiveIntegerField(default=0)
    date_publication = models.DateField()
    couverture = models.ImageField(upload_to='livres/couvertures/', null=True, blank=True)
    
    # Relation plusieurs-à-un (ForeignKey)
    # Un livre a un seul auteur principal, un auteur peut avoir écrit plusieurs livres
    auteur_principal = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,  # Si l'auteur est supprimé, ses livres le sont aussi
        related_name='livres'  # Pour accéder aux livres depuis l'auteur: auteur.livres.all()
    )
    
    # Relation plusieurs-à-plusieurs (ManyToManyField)
    # Un livre peut appartenir à plusieurs catégories, une catégorie peut contenir plusieurs livres
    categories = models.ManyToManyField(
        Categorie,
        related_name='livres'
    )
    
    # Relation plusieurs-à-plusieurs avec table intermédiaire personnalisée
    co_auteurs = models.ManyToManyField(
        Auteur,
        through='ContributionLivre',
        related_name='contributions',
        blank=True
    )
    
    def __str__(self):
        return self.titre


class ContributionLivre(models.Model):
    """
    Table intermédiaire pour la relation entre Livre et Auteur (co-auteurs)
    Permet d'ajouter des attributs à la relation
    """
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='Co-auteur')
    date_contribution = models.DateField(default=timezone.now)
    
    class Meta:
        unique_together = ('livre', 'auteur', 'role')  # Contrainte d'unicité
        verbose_name = "Contribution"
        verbose_name_plural = "Contributions"


class ProfilUtilisateur(models.Model):
    """
    Modèle de profil utilisateur avec relation un-à-un
    """
    utilisateur = models.OneToOneField(
        'auth.User',  # Modèle User intégré à Django
        on_delete=models.CASCADE,
        related_name='profil'
    )
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    photo_profil = models.ImageField(upload_to='profils/', null=True, blank=True)
    
    # Champs JSON pour stocker des préférences
    preferences = models.JSONField(default=dict)
    
    def __str__(self):
        return f"Profil de {self.utilisateur.username}"


class Emprunt(models.Model):
    """
    Modèle représentant l'emprunt d'un livre
    """
    livre = models.ForeignKey(Livre, on_delete=models.PROTECT)
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True, blank=True)
    
    STATUT_CHOICES = [
        ('E', 'Emprunté'),
        ('R', 'Retourné'),
        ('P', 'Perdu'),
        ('D', 'Retard'),
    ]
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES, default='E')
    
    def est_en_retard(self):
        """Vérifie si l'emprunt est en retard"""
        if not self.date_retour_effective and timezone.now().date() > self.date_retour_prevue:
            return True
        return False
    
    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.utilisateur.username}"
    
    class Meta:
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"
        ordering = ['-date_emprunt'] 