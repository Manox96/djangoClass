"""
Tableau regroupant les différents types de données de bases de SQL 
et leurs équivalents dans le modèle de DJANGO.
"""

# Types de texte
"""
CharField         -> VARCHAR        : Champ texte de longueur limitée
                     Exemple: models.CharField(max_length=100)

TextField         -> TEXT           : Champ texte long sans limite
                     Exemple: models.TextField()

EmailField        -> VARCHAR        : Champ validant une adresse email
                     Exemple: models.EmailField()

URLField          -> VARCHAR        : Champ validant une URL
                     Exemple: models.URLField()

SlugField         -> VARCHAR        : Champ pour les slugs URL (lettres, chiffres, underscores, traits d'union)
                     Exemple: models.SlugField()
"""

# Types numériques
"""
IntegerField      -> INTEGER        : Nombre entier
                     Exemple: models.IntegerField()

BigIntegerField   -> BIGINT         : Nombre entier de grande taille
                     Exemple: models.BigIntegerField()

FloatField        -> FLOAT          : Nombre à virgule flottante
                     Exemple: models.FloatField()

DecimalField      -> DECIMAL        : Nombre décimal à précision fixe
                     Exemple: models.DecimalField(max_digits=5, decimal_places=2)

PositiveIntegerField -> INTEGER     : Entier positif seulement
                     Exemple: models.PositiveIntegerField()
"""

# Types booléens
"""
BooleanField      -> BOOLEAN/TINYINT: Vrai/Faux (True/False)
                     Exemple: models.BooleanField(default=True)

NullBooleanField  -> BOOLEAN/TINYINT: Vrai/Faux/Null (True/False/None)
                     Exemple: models.NullBooleanField()
"""

# Types dates et heures
"""
DateField         -> DATE           : Date (année, mois, jour)
                     Exemple: models.DateField(auto_now_add=True)

TimeField         -> TIME           : Heure
                     Exemple: models.TimeField()

DateTimeField     -> DATETIME       : Date et heure
                     Exemple: models.DateTimeField(auto_now=True)

DurationField     -> INTERVAL       : Durée
                     Exemple: models.DurationField()
"""

# Types de clés
"""
AutoField         -> INTEGER        : Clé primaire auto-incrémentée
                     Exemple: id = models.AutoField(primary_key=True)

BigAutoField      -> BIGINT         : Grande clé primaire auto-incrémentée
                     Exemple: id = models.BigAutoField(primary_key=True)

ForeignKey        -> INTEGER + CONSTRAINT : Clé étrangère (relation plusieurs-à-un)
                     Exemple: models.ForeignKey(Auteur, on_delete=models.CASCADE)

OneToOneField     -> INTEGER + CONSTRAINT : Relation un-à-un
                     Exemple: models.OneToOneField(Profile, on_delete=models.CASCADE)

ManyToManyField   -> Table intermédiaire : Relation plusieurs-à-plusieurs
                     Exemple: models.ManyToManyField(Tag)
"""

# Types de fichiers
"""
FileField         -> VARCHAR        : Champ pour télécharger des fichiers
                     Exemple: models.FileField(upload_to='documents/')

ImageField        -> VARCHAR        : Champ pour télécharger des images
                     Exemple: models.ImageField(upload_to='images/')
"""

# Autres types
"""
JSONField         -> JSON/JSONB     : Stocke des données JSON
                     Exemple: models.JSONField()

UUIDField         -> UUID           : Stocke un UUID universellement unique
                     Exemple: models.UUIDField(default=uuid.uuid4)

BinaryField       -> BLOB/BYTEA     : Stocke des données binaires
                     Exemple: models.BinaryField()

GenericIPAddressField -> VARCHAR    : Stocke des adresses IPv4 ou IPv6
                     Exemple: models.GenericIPAddressField()
""" 