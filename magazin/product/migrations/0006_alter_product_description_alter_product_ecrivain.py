# Generated by Django 4.0.4 on 2022-06-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='ecrivain',
            field=models.CharField(max_length=50),
        ),
    ]
