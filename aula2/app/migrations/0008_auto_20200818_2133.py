# Generated by Django 3.1 on 2020-08-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200818_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salario',
            name='valor',
            field=models.FloatField(null=True),
        ),
    ]