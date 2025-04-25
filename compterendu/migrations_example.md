# Migrations Django : Guide Pratique

Les migrations Django permettent de gérer les changements de structure de base de données de manière structurée et reproductible.

## 1. Qu'est-ce qu'une migration ?

Une migration est un fichier Python qui décrit les changements à apporter à la base de données pour qu'elle corresponde à vos modèles. Django génère automatiquement ces fichiers lorsque vous modifiez vos modèles.

## 2. Commandes essentielles

### Créer des migrations

```bash
python manage.py makemigrations [app_name]
```

Cette commande examine vos modèles et crée des fichiers de migration pour les changements qu'elle détecte.

### Appliquer les migrations

```bash
python manage.py migrate [app_name] [migration_name]
```

Cette commande applique les migrations à la base de données.

### Lister les migrations

```bash
python manage.py showmigrations
```

Affiche toutes les migrations du projet et indique si elles ont été appliquées.

### Afficher le SQL d'une migration

```bash
python manage.py sqlmigrate app_name migration_name
```

Affiche le SQL que Django exécutera pour une migration donnée sans l'appliquer.

## 3. Exemple de cycle de vie des migrations

### Étape 1 : Créer un modèle initial

```python
# myapp/models.py
from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
```

### Étape 2 : Générer la migration initiale

```bash
python manage.py makemigrations myapp
```

Django crée un fichier comme `myapp/migrations/0001_initial.py`.

### Étape 3 : Appliquer la migration

```bash
python manage.py migrate myapp
```

### Étape 4 : Modifier le modèle

```python
# myapp/models.py
from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    en_stock = models.BooleanField(default=True)  # Nouveau champ
    categorie = models.CharField(max_length=50, null=True)  # Nouveau champ
```

### Étape 5 : Créer une nouvelle migration

```bash
python manage.py makemigrations myapp
```

Django crée un fichier comme `myapp/migrations/0002_produit_en_stock_produit_categorie.py`.

### Étape 6 : Appliquer la nouvelle migration

```bash
python manage.py migrate myapp
```

## 4. Migrations avec des champs qui nécessitent une valeur

Si vous ajoutez un champ qui ne peut pas être null et n'a pas de valeur par défaut, Django vous demandera quoi faire :

1. Fournir une valeur par défaut qui sera utilisée pour les enregistrements existants
2. Quitter et ajouter manuellement un défaut ou permettre les valeurs nulles

## 5. Migrations avec dépendances

Les migrations peuvent dépendre d'autres migrations, ce qui permet à Django de déterminer l'ordre d'exécution correct.

```python
# Exemple de dépendance dans un fichier de migration
dependencies = [
    ('myapp', '0001_initial'),
    ('another_app', '0003_add_field'),
]
```

## 6. Migrations manuelles

Parfois, vous devrez écrire des migrations personnalisées pour des opérations complexes. Vous pouvez créer un fichier de migration vide :

```bash
python manage.py makemigrations --empty myapp
```

Puis modifiez-le pour inclure vos opérations personnalisées :

```python
from django.db import migrations

def enregistrer_categories(apps, schema_editor):
    # Accéder au modèle géré par les migrations (pas directement au modèle)
    Produit = apps.get_model('myapp', 'Produit')
    for produit in Produit.objects.all():
        if not produit.categorie:
            produit.categorie = "Non classé"
            produit.save()

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_produit_en_stock_produit_categorie'),
    ]
    
    operations = [
        migrations.RunPython(enregistrer_categories),
    ]
```

## 7. Bonnes pratiques

1. **Toujours versionner les migrations** : Les migrations font partie de votre code et devraient être versionnées.
2. **Tester les migrations** : Avant de déployer en production, testez les migrations sur une copie de la base de données.
3. **Ne pas modifier les fichiers de migration** : Une fois qu'une migration a été appliquée, ne la modifiez pas ; créez plutôt une nouvelle migration.
4. **Garder les migrations petites** : Préférez plusieurs petites migrations à une seule grande.
5. **Faire des sauvegardes** : Avant d'appliquer des migrations en production, sauvegardez votre base de données.

## 8. Gérer les migrations en équipe

Si plusieurs développeurs ajoutent des migrations simultanément, des conflits peuvent survenir. La solution :

1. Fusionnez les branches de code
2. Exécutez `python manage.py makemigrations --merge`
3. Testez les migrations fusionnées 