from django import forms

from .models import Mia

    class MiaForm(forms.ModelForm):

        class Meta:
            model = Mia
            # fields = ('title', 'text',)
