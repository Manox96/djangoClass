#!/bin/bash

# Script d'installation pour Django Photo Gallery sur Ubuntu
# À exécuter à la racine du projet

echo "Installation de Django Photo Gallery sur Ubuntu..."

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 n'est pas installé. Installation en cours..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
fi

# Création de l'environnement virtuel
if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activation de l'environnement virtuel
echo "Activation de l'environnement virtuel..."
source venv/bin/activate

# Installation des dépendances système pour Pillow
echo "Installation des dépendances pour Pillow..."
sudo apt install -y libjpeg-dev zlib1g-dev

# Installation des dépendances Python
echo "Installation des dépendances Python..."
pip install -r requirements.txt

# Création du répertoire media si nécessaire
if [ ! -d "media/photos" ]; then
    echo "Création du répertoire media/photos..."
    mkdir -p media/photos
fi

# Configuration des permissions
echo "Configuration des permissions..."
chmod -R 755 media
sudo chown -R $USER:$USER media

# Application des migrations
echo "Application des migrations..."
python manage.py migrate

# Proposition de création d'un superutilisateur
echo ""
echo "Voulez-vous créer un superutilisateur ? (o/n)"
read create_superuser

if [ "$create_superuser" = "o" ] || [ "$create_superuser" = "O" ]; then
    python manage.py createsuperuser
fi

echo ""
echo "Installation terminée !"
echo "Pour lancer le serveur de développement, exécutez :"
echo "source venv/bin/activate && python manage.py runserver"
echo ""
echo "Accédez à l'application dans votre navigateur : http://127.0.0.1:8000/"

# Rendre le script exécutable pour la prochaine fois
chmod +x setup_ubuntu.sh 