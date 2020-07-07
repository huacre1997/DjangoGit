# Generated by Django 3.0.6 on 2020-05-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200526_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
