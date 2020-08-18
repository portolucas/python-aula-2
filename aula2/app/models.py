from django.db import models

# Create your models here.


"""
Para organizar os modelos em módulos podemos
criar uma classe que descreve como o modelo
será implementado.

Para criar modelos com herança podemos
receber como parâmetro o atributo Model de models, por exemplo.
Os tipos que models.Model oferecem são por exemplo:
- CharField, FileField, FloatField, JSONField, TimeField, etc.
A lista completa de fields pode ser encontrada aqui: 
https://docs.djangoproject.com/en/3.1/ref/models/fields/


"""
class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)

class Salario(models.Model):
    valor = models.FloatField(null=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)
    nacionalidade = models.CharField(max_length=30)
    depto_atual = models.ForeignKey(
        Departamento,
        on_delete=models.RESTRICT,
        null=True)
    hist_deptos = models.ManyToManyField(
        Departamento,
        related_name="hist_pessoa_depto"
    )
    hist_salarios = models.ManyToManyField(
        Salario,
        related_name="hist_pessoa_salario"
    )
    depto_chefia = models.OneToOneField(
        Departamento,
        on_delete=models.RESTRICT,
        null=True,
        related_name='chefia_depto',
    )
    
    SENIORIDADE_CHOICES = [
        ('T', 'Trainee'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior'),
    ]

    senioridade = models.CharField(
        max_length = 1,
        choices=SENIORIDADE_CHOICES,
        default='T'
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
