import rules

from frequencia.accounts.rules import is_gestor, is_bolsista
from frequencia.vinculos.utils import get_setores

#Predicates
@rules.predicate
def is_justificativa_author(user, justificativa):
	try:
		return justificativa.vinculo in user.vinculos.all()
	except:
		return None

@rules.predicate
def is_justificativa_chefe(user, justificativa):
	try:	
		user_setores = get_setores(user)
		return user.has_perm('accounts.is_coordenador_chefe') and justificativa.vinculo.setor in user_setores
	except:
		return None

@rules.predicate
def can_reabrir(user, justificativa):
	try:		
		return user.has_perm('accounts.is_gestor') and justificativa.status
	except:
		return None

@rules.predicate
def can_delete(user, justificativa):	
	try:		
		return is_justificativa_author(user, justificativa) and not justificativa.status
	except:
		return None
	

#Custom predicates
justificativa_viewer = is_justificativa_author | is_justificativa_chefe | is_gestor

#Rules
rules.add_perm('tipo_justificativa.can_manage', is_gestor)
rules.add_perm('justificativa.justificativa_author', is_justificativa_author)

rules.add_perm('justificativa.can_create', is_bolsista)
rules.add_perm('justificativa.can_view', justificativa_viewer)
rules.add_perm('justificativa.can_analyse', is_justificativa_chefe)
rules.add_perm('justificativa.can_reabrir', can_reabrir)
rules.add_perm('justificativa.can_delete', can_delete)