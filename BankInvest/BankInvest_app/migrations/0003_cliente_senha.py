# Generated by Django 4.2.1 on 2023-05-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankInvest_app', '0002_transacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default='pimentinhamalaguenta', max_length=12),
        ),
    ]