"""
Configuration des connexions avec différentes bases de données dans Django
"""

# Configuration par défaut avec SQLite (incluse dans settings.py)
DATABASES_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Configuration avec MySQL
DATABASES_MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nom_de_votre_base',
        'USER': 'utilisateur_mysql',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost',  # Ou adresse IP du serveur MySQL
        'PORT': '3306',       # Port par défaut de MySQL
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Configuration avec PostgreSQL
DATABASES_POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_votre_base',
        'USER': 'utilisateur_postgres',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost',  # Ou adresse IP du serveur PostgreSQL
        'PORT': '5432',       # Port par défaut de PostgreSQL
    }
}

# Configuration avec SQL Server
DATABASES_SQLSERVER = {
    'default': {
        'ENGINE': 'mssql',    # Nécessite le paquet 'django-mssql-backend'
        'NAME': 'nom_de_votre_base',
        'USER': 'utilisateur_sqlserver',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost\\SQLEXPRESS',  # Nom du serveur SQL Server
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Dépend du driver installé
        },
    }
}

# Configuration avec Oracle
DATABASES_ORACLE = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',                    # SID Oracle
        'USER': 'utilisateur_oracle',
        'PASSWORD': 'mot_de_passe',
        'HOST': 'localhost',
        'PORT': '1521',                  # Port par défaut d'Oracle
    }
}

"""
Dépendances à installer:

# Pour MySQL
pip install mysqlclient

# Pour PostgreSQL
pip install psycopg2-binary

# Pour SQL Server
pip install django-mssql-backend

# Pour Oracle
pip install cx_Oracle
"""


"""
UTILISATION DE PLUSIEURS BASES DE DONNÉES
----------------------------------------

Django permet de configurer plusieurs bases de données dans le même projet:
"""

MULTIPLE_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'utilisateurs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_utilisateurs',
        'USER': 'user_mysql',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'produits': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_produits',
        'USER': 'user_postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

"""
Routage de base de données - database_routers.py
"""

class UtilisateursRouter:
    """
    Routeur pour diriger les requêtes liées aux utilisateurs
    vers la base de données 'utilisateurs'.
    """
    def db_for_read(self, model, **hints):
        # Dirige les lectures vers 'utilisateurs' si le modèle est dans l'app 'utilisateurs'
        if model._meta.app_label == 'utilisateurs':
            return 'utilisateurs'
        return None

    def db_for_write(self, model, **hints):
        # Dirige les écritures vers 'utilisateurs' si le modèle est dans l'app 'utilisateurs'
        if model._meta.app_label == 'utilisateurs':
            return 'utilisateurs'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Autorise les relations si les deux objets sont dans l'app 'utilisateurs'
        if obj1._meta.app_label == 'utilisateurs' and obj2._meta.app_label == 'utilisateurs':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Autorise les migrations pour l'app 'utilisateurs' dans la base 'utilisateurs'
        if app_label == 'utilisateurs' and db == 'utilisateurs':
            return True
        # Empêche les migrations de l'app 'utilisateurs' dans les autres bases
        elif app_label == 'utilisateurs':
            return False
        return None


"""
Configuration du routeur dans settings.py:
"""
DATABASE_ROUTERS = ['myproject.database_routers.UtilisateursRouter'] 