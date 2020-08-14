# Generated by Django 3.1 on 2020-08-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200814_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='escolaridade',
            field=models.CharField(choices=[('NI', 'Não informado'), ('EF', 'Ensino Fundamental'), ('EM', 'Ensino Médio'), ('ES', 'Ensino Superior')], default='NI', max_length=2),
        ),
    ]