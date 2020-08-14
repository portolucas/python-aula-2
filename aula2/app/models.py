from django.db import models

# Create your models here.


class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)
    depto_atual = models.ForeignKey(
        Departamento,
        on_delete=models.RESTRICT,
        null=True)
    hist_deptos = models.ManyToManyField(
        Departamento,
        related_name="hist_pessoa_depto"
    )

    depto_chefia = models.OneToOneField(
        Departamento,
        on_delete=models.RESTRICT,
        null=True,
        related_name='chefia_depto',
    )

    ESCOLARIDADE_CHOICES = [
        ('NI', 'Não informado'),
        ('EF', 'Ensino Fundamental'),
        ('EM', 'Ensino Médio'),
        ('ES', 'Ensino Superior'),
    ]

    escolaridade = models.CharField(
        max_length=2,
        choices=ESCOLARIDADE_CHOICES,
        default='NI'
    )
