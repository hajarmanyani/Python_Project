# Generated by Django 4.0.4 on 2022-06-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fourn',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=30)),
                ('Tel', models.IntegerField()),
                ('Adresse', models.CharField(max_length=150)),
                ('Cin', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
            ],
        ),
    ]
