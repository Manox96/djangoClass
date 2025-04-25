# Guide d'installation complète sur Ubuntu

Ce guide vous aidera à installer le projet Photo Gallery sur un système Ubuntu où rien n'est encore installé.

## Étape 1 : Installation des dépendances système

Ouvrez un terminal (Ctrl+Alt+T) et exécutez ces commandes pour installer les prérequis :

```bash
# Mettre à jour votre système
sudo apt update
sudo apt upgrade -y

# Installer Python et les outils nécessaires
sudo apt install -y python3 python3-pip python3-venv git
```

## Étape 2 : Installation des dépendances pour Pillow (traitement d'images)

```bash
sudo apt install -y libjpeg-dev zlib1g-dev python3-dev
```

## Étape 3 : Récupérer le projet

Si vous avez reçu une archive du projet (ZIP ou tarball), décompressez-la :

```bash
# Si vous avez un fichier .zip
unzip photo-gallery.zip -d photo-gallery

# Si vous avez un fichier .tar.gz
tar -xzf photo-gallery.tar.gz
```

Si le projet est sur GitHub :

```bash
git clone https://github.com/username/photo-gallery.git
```

## Étape 4 : Configurer l'environnement Python

```bash
# Accéder au répertoire du projet
cd photo-gallery  # Ou le nom du dossier extrait

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate
```

## Étape 5 : Installer les dépendances Python

```bash
# Installer Django et Pillow
pip install Django
pip install Pillow

# Alternative : si un fichier requirements.txt existe
pip install -r requirements.txt
```

## Étape 6 : Configurer la base de données

```bash
# Créer les tables dans la base de données
python manage.py migrate
```

## Étape 7 : Créer un utilisateur administrateur (optionnel)

```bash
python manage.py createsuperuser
# Suivre les instructions à l'écran pour créer un compte admin
```

## Étape 8 : Configurer les fichiers statiques et média

```bash
# Créer les dossiers nécessaires
mkdir -p media/photos
mkdir -p static

# Appliquer les permissions
chmod -R 755 media
chmod -R 755 static
```

## Étape 9 : Lancer le serveur de développement

```bash
python manage.py runserver
```

Ouvrez votre navigateur et accédez à : http://127.0.0.1:8000/

## Guide de dépannage

### Si vous rencontrez des erreurs de module manquant :

```bash
# Vérifiez que vous êtes dans l'environnement virtuel (venv)
source venv/bin/activate

# Puis installez le module manquant
pip install nom-du-module
```

### Si vous avez des problèmes d'accès aux dossiers média :

```bash
# Assurez-vous que les permissions sont correctes
sudo chown -R $USER:$USER media
chmod -R 755 media
```

### Si Django ne trouve pas le module Pillow :

```bash
# Désinstallez puis réinstallez Pillow avec les bons paramètres
pip uninstall Pillow
pip install Pillow
```

## Installation en production (optionnel)

Si vous souhaitez déployer l'application en production, suivez ces étapes supplémentaires :

### 1. Installer Nginx et Gunicorn

```bash
sudo apt install -y nginx
pip install gunicorn
```

### 2. Configurer Nginx

Créez un fichier de configuration pour Nginx :

```bash
sudo nano /etc/nginx/sites-available/photo-gallery
```

Ajoutez ce contenu (remplacez les chemins selon votre installation) :

```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/your_username/photo-gallery;
    }
    
    location /media/ {
        root /home/your_username/photo-gallery;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Activez la configuration et redémarrez Nginx :

```bash
sudo ln -s /etc/nginx/sites-available/photo-gallery /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 3. Configurer Gunicorn comme service

Créez un fichier de service systemd :

```bash
sudo nano /etc/systemd/system/gunicorn-photo-gallery.service
```

Ajoutez ce contenu :

```ini
[Unit]
Description=Gunicorn daemon for Photo Gallery
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/home/your_username/photo-gallery
ExecStart=/home/your_username/photo-gallery/venv/bin/gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

Activez et démarrez le service :

```bash
sudo systemctl enable gunicorn-photo-gallery
sudo systemctl start gunicorn-photo-gallery
sudo systemctl status gunicorn-photo-gallery
```

## Commandes utiles

- Lancer le serveur : `python manage.py runserver`
- Créer un administrateur : `python manage.py createsuperuser`
- Appliquer les migrations : `python manage.py migrate`
- Activer l'environnement virtuel : `source venv/bin/activate`
- Quitter l'environnement virtuel : `deactivate`

## Conclusion

Votre application Photo Gallery devrait maintenant être opérationnelle sur votre système Ubuntu. Vous pouvez accéder à l'interface principale via http://127.0.0.1:8000/ et commencer à télécharger vos photos.

Pour toute aide supplémentaire, n'hésitez pas à consulter la documentation officielle de Django (https://docs.djangoproject.com/). 