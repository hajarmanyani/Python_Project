# Generated by Django 4.0.4 on 2022-06-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auteur', '0001_initial'),
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='auteur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Auteur.auteur'),
        ),
    ]
