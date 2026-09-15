from django.db import models

# --------------------------------------------------------
# 1. TABLE DES PAYS (Accounts Countries)
# --------------------------------------------------------
class Country(models.Model):
    # La clé primaire ici n'est pas un ID numérique, mais le code du pays (ex: 'FR', 'US')
    code = models.CharField(max_length=2, primary_key=True, db_column='code')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Countries'
        managed = False

    def __str__(self):
        return self.name


# --------------------------------------------------------
# 2. TABLE DES ADRESSES (Accounts Addresses)
# --------------------------------------------------------
class Address(models.Model):
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    address_line3 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # 🔗 Relation (Flèche verte) : Une adresse est liée à un pays
    country = models.ForeignKey(
        Country, 
        on_delete=models.SET_NULL, 
        blank=True, null=True, 
        db_column='country_code'
    )
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Addresses'
        managed = False

    def __str__(self):
        return f"{self.address_line1}, {self.city}"


# --------------------------------------------------------
# 3. TABLE DES AVATARS (Accounts Avatars)
# --------------------------------------------------------
class Avatar(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    data = models.BinaryField()  # mediumblob
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Avatars'
        managed = False

    def __str__(self):
        return self.name


# --------------------------------------------------------
# 4. TABLE DES UTILISATEURS (Accounts Users)
# --------------------------------------------------------
class UserAccount(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'En attente'
        ACTIVE = 'active', 'Actif'
        SUSPENDED = 'suspended', 'Suspendu'
        LOCKED = 'locked', 'Verrouillé'

    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # 🔗 Relations (Flèches rouge et verte) : Utilisateur -> Adresse et Utilisateur -> Avatar
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, blank=True, null=True, db_column='address_id'
    )
    avatar = models.ForeignKey(
        Avatar, on_delete=models.SET_NULL, blank=True, null=True, db_column='avatar_id'
    )

    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    failed_login_attempts = models.PositiveIntegerField(default=0)
    locked_until = models.DateTimeField(blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    
    two_factor_enabled = models.BooleanField(default=False)
    two_factor_secret = models.CharField(max_length=255, blank=True, null=True)
    
    deleted_at = models.DateTimeField(blank=True, null=True)
    account_expires_at = models.DateTimeField(blank=True, null=True)
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    terms_version = models.CharField(max_length=20, blank=True, null=True)
    
    email_unique = models.CharField(max_length=255, blank=True, null=True)
    nickname_unique = models.CharField(max_length=50, blank=True, null=True)
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Users'
        managed = False

    def __str__(self):
        return self.email


# --------------------------------------------------------
# 5. TABLE D'HISTORIQUE DE CONNEXION (Accounts LoginHistory)
# --------------------------------------------------------
class LoginHistory(models.Model):
    class StatusChoices(models.TextChoices):
        SUCCESS = 'success', 'Succès'
        FAILED = 'failed', 'Échec'
        BLOCKED = 'blocked', 'Bloqué'

    # 🔗 Relation (Flèche bleue) : Historique -> Utilisateur
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, db_column='user_id'
    )
    
    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.CharField(max_length=500, blank=True, null=True)
    
    # 🔗 Relation (Flèche verte) : Historique -> Pays
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True, db_column='country_code'
    )
    
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'LoginHistory'
        managed = False