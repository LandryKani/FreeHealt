# Generated by Django 3.2.8 on 2021-11-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jour',
            fields=[
                ('idJour', models.AutoField(primary_key=True, serialize=False)),
                ('dateJour', models.DateField()),
            ],
        ),
    ]
