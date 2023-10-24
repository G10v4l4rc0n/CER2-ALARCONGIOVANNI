# Generated by Django 4.2.6 on 2023-10-24 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=200)),
                ('detalle_corto', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('S', 'suspensión de actividades'), ('C', 'suspensión de clases'), ('I', 'información')], default='I', max_length=30)),
                ('visible', models.BooleanField(default=False)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.entidad')),
            ],
        ),
    ]
