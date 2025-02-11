from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    prioridade = models.CharField(
        max_length=10,
        choices=[('Alta', 'Alta'), ('Média', 'Média'), ('Baixa', 'Baixa')]
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas', db_column='usuario_id')

    def __str__(self):
        return f"{self.descricao} - {self.usuario.nome if self.usuario else 'Sem usuário'}"
