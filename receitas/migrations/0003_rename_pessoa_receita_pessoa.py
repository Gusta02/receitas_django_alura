# Generated by Django 3.2.9 on 2021-11-25 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='Pessoa',
            new_name='pessoa',
        ),
    ]
