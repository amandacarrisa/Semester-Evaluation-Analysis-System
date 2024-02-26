from curses.ascii import US
from dataclasses import field
from django import forms
from .models import EdomAdmin

class CreateEdomAdmin(forms.ModelForm):

    id_admin = forms.CharField(required=True)

    class Meta:
        model = EdomAdmin
        fields = ['id_admin']