# Semaine 2 : Django et les bases de données

Ce compte rendu présente les concepts de base de données dans Django avec des exemples pratiques.

## Sommaire
1. [Création d'Application](#création-dapplication)
2. [Création de Modèle](#création-de-modèle)
3. [Création des migrations](#création-des-migrations)
4. [Configuration des connexions avec d'autres bases de données](#configuration-des-connexions)

## Création d'Application
Une application Django est un composant fonctionnel de votre projet qui contient des modèles, vues, et autres éléments.

```bash
python manage.py startapp nom_app
```

## Création de Modèle
### Qu'est-ce qu'un modèle ?
Un modèle Django est une classe Python qui représente une table dans la base de données. Il définit la structure des données.

### Où créer votre modèle ?
Les modèles sont définis dans le fichier `models.py` de votre application Django.

### Types de données dans Django

Consultez le fichier [types_donnees.py](types_donnees.py) pour un tableau complet des types de données.

### Exemple de modèle

Consultez les fichiers :
- [models_example.py](models_example.py) pour un exemple de modèle de base
- [models_avance.py](models_avance.py) pour des exemples plus avancés avec relations

## Création des migrations

### Qu'est-ce qu'une migration ?
Une migration est un fichier Python qui décrit les changements à apporter à la base de données pour qu'elle corresponde à vos modèles.

### Comment définir une migration sur Django ?
```bash
# Créer les fichiers de migration
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate
```

Pour des exemples détaillés, consultez [migrations_example.md](migrations_example.md).

## Configuration des connexions
### Comment configurer la connexion avec une autre base de données (MySQL, SQL SERVER)

Pour configurer Django avec différentes bases de données, modifiez le dictionnaire `DATABASES` dans `settings.py`.

Pour des exemples détaillés, consultez [config_database.py](config_database.py).

## Projet pratique
Le fichier [projet_pratique.md](projet_pratique.md) contient un exercice complet pour créer un modèle et ses migrations. 