# Generated by Django 4.2.6 on 2023-10-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0003_rename_tiposdeexames_tipos_de_exames'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposExames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('I', 'Exames de imagem'), ('S', 'Exames de sangue')], max_length=1)),
                ('preco', models.FloatField()),
                ('disponivel', models.BooleanField(default=True)),
                ('horario_inicial', models.IntegerField()),
                ('horario_final', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tipos_de_Exames',
        ),
    ]
