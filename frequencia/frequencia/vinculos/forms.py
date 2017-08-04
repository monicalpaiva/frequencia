from django import forms

from .models import Setor, Coordenadoria

class VinculoForm(forms.ModelForm):

	groups = forms.ModelMultipleChoiceField(
			label='Papéis do usuário',
            widget=forms.CheckboxSelectMultiple,
            queryset=Group.objects.all(),
            )

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['name', 'username', 'email', 'cpf', 'is_active']


class EditSetorForm(forms.ModelForm):

	class Meta:
		model = Setor
		fields = ['nome', 'chefes', 'coordenadoria',]

class EditCoordenadoriaForm(forms.ModelForm):

	class Meta:
		model = Coordenadoria
		fields = ['nome', 'coordenadores',]