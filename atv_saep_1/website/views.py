from django.shortcuts import render, redirect
from .models import Usuario, Tarefa

def home(request):
    return render(request, 'home.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']
        Usuario.objects.create(nome=nome, senha=senha)
        return redirect('home')
    return render(request, 'cadastro_usuario.html')

def cadastro_tarefa(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        setor = request.POST['setor']
        prioridade = request.POST['prioridade']
        Tarefa.objects.create(descricao=descricao, setor=setor, prioridade=prioridade)
        return redirect('home')
    return render(request, 'cadastro_tarefa.html')
