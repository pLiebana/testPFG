# Generated by Django 4.2.1 on 2023-06-09 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aula_alter_clasehorario_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasehorario',
            name='profesor',
            field=models.ForeignKey(limit_choices_to={'tipo_usuario': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuarioextendido'),
        ),
    ]
