# Django Photo Gallery - Guide d'installation pour Ubuntu

Ce guide vous aidera à installer et configurer l'application Django Photo Gallery sur un système Ubuntu.

## Prérequis

Assurez-vous que les paquets suivants sont installés sur votre système Ubuntu :

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-dev libpq-dev build-essential
```

## Installation

1. Clonez le dépôt ou téléchargez et extrayez l'archive du projet.

2. Ouvrez un terminal et naviguez vers le répertoire du projet :
   ```bash
   cd chemin/vers/djangoClass
   ```

3. Créez un environnement virtuel Python :
   ```bash
   python3 -m venv venv
   ```

4. Activez l'environnement virtuel :
   ```bash
   source venv/bin/activate
   ```

5. Installez les dépendances :
   ```bash
   pip install django
   pip install Pillow  # Nécessaire pour gérer les images
   ```

6. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

7. Créez un superutilisateur (facultatif pour l'administration) :
   ```bash
   python manage.py createsuperuser
   ```

8. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

9. Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:8000/

## Structure des fichiers média

Sur Ubuntu, les fichiers média sont stockés dans le répertoire `media/photos/` à la racine du projet. Assurez-vous que ce répertoire existe et a les permissions appropriées :

```bash
mkdir -p media/photos
chmod -R 755 media
```

## Résolution des problèmes courants sur Ubuntu

### Problèmes de permissions

Si vous rencontrez des problèmes de permission lors de l'upload d'images :

```bash
# À exécuter depuis le répertoire du projet
sudo chown -R $USER:$USER media
chmod -R 755 media
```

### Installation de Pillow

Si l'installation de Pillow échoue, installez ces dépendances supplémentaires :

```bash
sudo apt install libjpeg-dev zlib1g-dev
pip install Pillow
```

### Servir l'application en production

Pour une configuration de production sur Ubuntu avec Nginx et Gunicorn :

1. Installez Nginx et Gunicorn :
   ```bash
   sudo apt install nginx
   pip install gunicorn
   ```

2. Créez un fichier de configuration Nginx dans `/etc/nginx/sites-available/` :
   ```
   server {
       listen 80;
       server_name votre_domaine_ou_ip;
       
       location /static/ {
           alias /chemin/vers/djangoClass/static/;
       }
       
       location /media/ {
           alias /chemin/vers/djangoClass/media/;
       }
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

3. Activez le site et redémarrez Nginx :
   ```bash
   sudo ln -s /etc/nginx/sites-available/votre_config /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

4. Lancez l'application avec Gunicorn :
   ```bash
   gunicorn --bind 127.0.0.1:8000 myproject.wsgi
   ```

## Fonctionnalités de l'application

- Galerie de photos avec affichage dynamique
- Upload d'images avec formulaire intuitif
- Multiples vues pour afficher les photos (détails, liste, etc.)
- Interface responsive basée sur Bootstrap

## Captures d'écran

Pour voir l'application en action, visitez les URLs suivantes après avoir lancé le serveur :

- Page d'accueil : http://127.0.0.1:8000/
- Liste des photos : http://127.0.0.1:8000/photos/
- Upload de photo : http://127.0.0.1:8000/upload/
- Administration : http://127.0.0.1:8000/admin/

## Automatisation du déploiement (avec systemd)

Pour que l'application démarre automatiquement au démarrage du système :

1. Créez un fichier service systemd :
   ```bash
   sudo nano /etc/systemd/system/djangophoto.service
   ```

2. Ajoutez la configuration suivante :
   ```
   [Unit]
   Description=Django Photo Gallery Application
   After=network.target

   [Service]
   User=votre_utilisateur
   Group=votre_groupe
   WorkingDirectory=/chemin/vers/djangoClass
   Environment="PATH=/chemin/vers/djangoClass/venv/bin"
   ExecStart=/chemin/vers/djangoClass/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 myproject.wsgi

   [Install]
   WantedBy=multi-user.target
   ```

3. Activez et démarrez le service :
   ```bash
   sudo systemctl enable djangophoto
   sudo systemctl start djangophoto
   ```

4. Vérifiez l'état du service :
   ```bash
   sudo systemctl status djangophoto
   ``` 