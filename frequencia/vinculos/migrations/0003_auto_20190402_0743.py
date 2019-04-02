# Generated by Django 2.1.7 on 2019-04-02 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vinculos', '0002_auto_20171103_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='coordenadoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='setores', to='vinculos.Coordenadoria', verbose_name='Coordenadoria'),
        ),
        migrations.AlterField(
            model_name='vinculo',
            name='coordenadoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vinculos', to='vinculos.Coordenadoria', verbose_name='Coordenadoria'),
        ),
        migrations.AlterField(
            model_name='vinculo',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vinculos', to='auth.Group', verbose_name='Papel'),
        ),
        migrations.AlterField(
            model_name='vinculo',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vinculos', to='vinculos.Setor', verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='vinculo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vinculos', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]