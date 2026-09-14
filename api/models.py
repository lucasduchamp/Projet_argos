from django.db import models

# blank : accepte que le formulaire soit pas rempli 
# null : accepte que la bdd soit pas rempli 



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
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    address_id = models.PositiveIntegerField(blank=True, null=True)
    avatar_id = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    email_verified_at = models.DateTimeField(blank=True, null=True)
    failed_login_attempts = models.PositiveSmallIntegerField(default=0)
    locked_until = models.DateTimeField(blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)

    two_factor_enabled = models.BooleanField(default=False)
    two_factor_secret = models.CharField(max_length=255, blank=True, null=True)

    deleted_at = models.DateTimeField(blank=True, null=True)
    account_expires_at = models.DateTimeField(blank=True, null=True)
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    terms_version = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# La class Meta sert à configurer les options globales du modèle plutôt que ses champs individuels.

#Ici, elle force Django à cibler une table existante nommée Users (db_table = 'Users') et lui interdit d'en
# gérer la structure via les migrations (managed = False).

    class Meta:
        db_table = 'Users'
        managed = False



    def __str__(self):
        return self.email or f'User #{self.pk}'


class Avatar(models.Model):
    # id = models.AutoField(primary_key=True)  # Géré automatiquement par Django pour 'id: int(10) unsigned'
    name = models.CharField(max_length=100)
    data = models.BinaryField()  # Correspond au type SQL 'mediumblob'
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Avatars'
        managed = False

    def __str__(self):
        return self.name