from rules.contrib.views import PermissionRequiredMixin

from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect


from .models import Setor, Coordenadoria
from .forms import EditSetorForm, EditCoordenadoriaForm

#Views de setores
class SetoresCoordenadoriasListView(PermissionRequiredMixin, ListView):

 	model = Setor
 	template_name = 'setor_coordenadoria/setores_coordenadorias.html'
 	permission_required = 'accounts.is_gestor'

 	def get_context_data(self, **kwargs):
 		context = super(SetoresCoordenadoriasListView, self).get_context_data(**kwargs)
 		context['coordenadorias'] = Coordenadoria.objects.all()
 		return context


class SetorCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):

	model = Setor
	form_class = EditSetorForm
	template_name = 'setor_coordenadoria/setor_create_edit.html'
	permission_required = 'accounts.is_gestor'

	success_message = 'Setor cadastrado com sucesso!'

	def get_success_url(self):
		return reverse('vinculos:setores_coordenadorias')


class SetorUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):

	model = Setor
	form_class = EditSetorForm
	template_name = 'setor_coordenadoria/setor_create_edit.html'
	permission_required = 'accounts.is_gestor'	
	
	success_message = 'Setor atualizado com sucesso!'

	def get_success_url(self):
		return reverse('vinculos:setores_coordenadorias')

	def get_context_data(self, **kwargs):
		context = super(SetorUpdateView, self).get_context_data(**kwargs)

		context['coordenadores'] = self.object.coordenadoria.vinculos.filter(group__name='Coordenador', ativo=True)
		context['chefes'] = self.object.vinculos.filter(group__name='Chefe de setor', ativo=True)
		context['bolsistas'] = self.object.vinculos.filter(group__name='Bolsista', ativo=True)

		return context


class CoordenadoriaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):

	model = Coordenadoria
	form_class = EditCoordenadoriaForm
	template_name = 'setor_coordenadoria/coordenadoria_create_edit.html'
	permission_required = 'accounts.is_gestor'

	success_message = 'Coordenadoria cadastrada com sucesso!'

	def get_success_url(self):
		return reverse('vinculos:setores_coordenadorias')


class CoordenadoriaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):

	model = Coordenadoria
	form_class = EditCoordenadoriaForm
	template_name = 'setor_coordenadoria/coordenadoria_create_edit.html'
	permission_required = 'accounts.is_gestor'
	
	success_message = 'Coordenadoria atualizada com sucesso!'

	def get_success_url(self):
		return reverse('vinculos:setores_coordenadorias')

	def get_context_data(self, **kwargs):
		context = super(CoordenadoriaUpdateView, self).get_context_data(**kwargs)

		context['setores'] = self.object.setores.all()

		return context

# setores = SetoresListView.as_view()
setor_create = SetorCreateView.as_view()
setor_edit = SetorUpdateView.as_view()

# coordenadorias = CoordenadoriasListView.as_view()
coordenadoria_create = CoordenadoriaCreateView.as_view()
coordenadoria_edit = CoordenadoriaUpdateView.as_view()

setores_coordenadorias = SetoresCoordenadoriasListView.as_view()