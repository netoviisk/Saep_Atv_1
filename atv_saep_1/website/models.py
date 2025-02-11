from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('Alta', 'Alta'),
        ('Média', 'Média'),
        ('Baixa', 'Baixa'),
    ]

    id_tarefa = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES)

    def __str__(self):
        return self.descricao

