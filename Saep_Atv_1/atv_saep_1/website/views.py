from django.shortcuts import render, redirect
from .models import Usuario, Tarefa

def home(request):
    return render(request, 'Website/home.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']
        if nome and senha:  # Garante que os campos estão preenchidos
            Usuario.objects.create(nome=nome, senha=senha)
            return redirect('home')  # Redireciona para a home após salvar
    return render(request, 'Website/cadastro_usuario.html')

def cadastro_tarefa(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        setor = request.POST.get("setor")
        prioridade = request.POST.get("prioridade")
        usuario_id = request.POST.get("usuario_id")  # Pega o ID do usuário do formulário

        if not usuario_id:  # Verifica se usuario_id está vazio
            return render(request, "Website/cadastro_tarefa.html", {"error": "Selecione um usuário."})

        usuario = Usuario.objects.get(id_usuario=usuario_id)  # Busca o usuário no banco

        tarefa = Tarefa(descricao=descricao, setor=setor, prioridade=prioridade, usuario=usuario)
        tarefa.save()

        return redirect("lista_usuarios")  # Redireciona após salvar

    usuarios = Usuario.objects.all()
    return render(request, "Website/cadastro_tarefa.html", {"usuarios": usuarios})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()

    # Criar uma lista de dicionários contendo os usuários e suas tarefas
    dados_usuarios = []
    for usuario in usuarios:
        tarefas = Tarefa.objects.filter(usuario=usuario)
        if tarefas.exists():
            dados_usuarios.append({
                "usuario": usuario,
                "tarefas": tarefas
            })
        else:
            dados_usuarios.append({
                "usuario": usuario,
                "tarefas": None  # Indica que não há tarefas para este usuário
            })

    return render(request, 'Website/lista_usuarios.html', {'dados_usuarios': dados_usuarios})


