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
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password_hash': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'address_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'avatar_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'two_factor_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }