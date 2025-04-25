#!/bin/bash

# Script d'installation automatique pour Photo Gallery sur Ubuntu
# À exécuter avec: bash ubuntu_install.sh

echo "====== Installation de Photo Gallery sur Ubuntu ======"
echo "Ce script va installer tous les éléments nécessaires pour le projet."
echo ""

# Vérifier si on est bien sur Ubuntu
if [ ! -f /etc/lsb-release ]; then
    echo "Ce script est conçu pour Ubuntu. Votre système ne semble pas être Ubuntu."
    exit 1
fi

# Mettre à jour le système
echo "=== Mise à jour du système ==="
sudo apt update
sudo apt upgrade -y

# Installer les dépendances système
echo "=== Installation des dépendances système ==="
sudo apt install -y python3 python3-pip python3-venv git libjpeg-dev zlib1g-dev python3-dev

# Créer l'environnement virtuel
echo "=== Configuration de l'environnement Python ==="
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances Python
echo "=== Installation des dépendances Python ==="
pip install Django
pip install Pillow

# Si un requirements.txt existe, utiliser celui-ci
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Créer les dossiers nécessaires
echo "=== Configuration des dossiers média et statiques ==="
mkdir -p media/photos
mkdir -p static
chmod -R 755 media
chmod -R 755 static

# Appliquer les migrations
echo "=== Configuration de la base de données ==="
python manage.py migrate

# Proposer de créer un superutilisateur
echo ""
echo "Voulez-vous créer un compte administrateur ? (o/n)"
read create_admin

if [ "$create_admin" = "o" ] || [ "$create_admin" = "O" ]; then
    python manage.py createsuperuser
fi

# Collecter les fichiers statiques (si nécessaire)
echo "=== Collecte des fichiers statiques ==="
python manage.py collectstatic --noinput

echo ""
echo "====== Installation terminée ! ======"
echo "Pour lancer l'application:"
echo "1. Activez l'environnement virtuel: source venv/bin/activate"
echo "2. Lancez le serveur: python manage.py runserver"
echo ""
echo "Puis accédez à l'application dans votre navigateur: http://127.0.0.1:8000/"
echo ""

# Proposer de lancer directement le serveur
echo "Voulez-vous lancer le serveur maintenant ? (o/n)"
read start_server

if [ "$start_server" = "o" ] || [ "$start_server" = "O" ]; then
    python manage.py runserver
fi 