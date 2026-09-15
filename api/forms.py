from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'email',
            'password_hash',
            'nickname',
            'phone_number',
            'birth_date',
            'status',
            'address_id',
            'avatar_id',
            'two_factor_enabled',
        ]
        labels = {
            'password_hash': 'Mot de passe (brut)',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'birth_date': 'Date de naissance',
            'nickname': 'Pseudo',
            'phone_number': 'Téléphone',
            'address_id': 'ID Adresse',
            'avatar_id': 'ID Avatar',
            'two_factor_enabled': '2FA Activé',
        }