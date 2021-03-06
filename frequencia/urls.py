"""frequencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('frequencia.core.urls', namespace='core')),
    path('registro/', include('frequencia.registro.urls', namespace='registro')),
    path('vinculos', include('frequencia.vinculos.urls', namespace='vinculos')),
    path('calendario/', include('frequencia.calendario.urls', namespace='calendario')),
    path('justificativas/', include('frequencia.justificativas.urls', namespace='justificativas')),
    path('relatorios/', include('frequencia.relatorios.urls', namespace='relatorios')),
    path('conta/', include('frequencia.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^', include('frequencia.core.urls', namespace='core')),
#     url(r'^registro/', include('frequencia.registro.urls', namespace='registro')),
#     url(r'^vinculos/', include('frequencia.vinculos.urls', namespace='vinculos')),
#     url(r'^calendario/', include('frequencia.calendario.urls', namespace='calendario')),
# 	url(r'^justificativas/', include('frequencia.justificativas.urls', namespace='justificativas')),
# 	url(r'^relatorios/', include('frequencia.relatorios.urls', namespace='relatorios')),

#     url(r'^admin/', admin.site.urls),
#     url(r'^conta/', include('frequencia.accounts.urls', namespace='accounts')),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)