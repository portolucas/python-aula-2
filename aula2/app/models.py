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

    """
    _str_ é um método "mágico" do Python que define o que deve
    ser retornado se você chamar str() sobre um objeto. 
    O Django usa str(obj) em vários lugares, mais notavelmente 
    como um valor mostrado para renderizar um objeto no site de 
    administração do Django e como valores inseridos em um template 
    quando é mostrado um objeto. Por isso, que você deve sempre 
    retornar uma string, legível para humanos, dos métodos __str__.
    """

    def __str__(self):
        return smart_str('%s %s' % (self.nome, self.sobrenome))

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
        max_length=1,
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


"""
O Proxy serve por exemplo, para criar, excluir e
atualizar instâncias do modelo proxy e ainda assim
salvar todos os dados como se estivessemos usando
o modelo original (sem proxy [proxy=False]).

A diferença é que podemos alterar coisas como
a ordem do modelo padrão ou o gerenciador
padrão no proxy, sem ter que alterar o original.

Os modelos proxy são declarados como modelos normais.
Dizemos ao Django que é um modelo proxy atributo
da classe Meta para True.
https://docs.djangoproject.com/en/3.1/topics/db/models/#proxy-models
"""


class OrdenarPessoa(Pessoa):
    class Meta:
        ordering = ["nome"]
        proxy = True

"""
Relacionamentos

Relacionamento 1-1 (OneToOneField)

Assim como o próprio nome supuõe, o relacionamento 1-1 define
que um item de uma entidade só poderá se relacionar com um
item de outra entidade. Por exemplo, um departamento só
pode ter uma chefia, assim como cada chefe só pode chefiar
um departamento.

Relacionamento 1N (ForeignKey)

O relacionamento 1N determina que um item de uma tabela 
pode se relacionar com vários itens de uma outra tabela.
Por exemplo, uma pessoa pode passar por diversos departamentos,
porém ela só pode ter um departamento atual.

Relacionamento NN (ManyToManyField)

O relacionam define que um item de uma tabela pode se 
relacionar com vários itens de uma outra tablea e vice-versa.

Por exemplo, uma pessoa pode ser vinculada a diversos departamentos
e departamentos podem ter várias pessoas.

"""
