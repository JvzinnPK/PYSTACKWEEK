# Generated by Django 4.2.6 on 2023-10-07 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0002_tiposdeexames_delete_tiposexames'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TiposdeExames',
            new_name='Tipos_de_Exames',
        ),
    ]
