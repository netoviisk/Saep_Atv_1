from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_tarefa/', views.cadastro_tarefa, name='cadastro_tarefa'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('excluir_usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('excluir_tarefas_usuario/<int:usuario_id>/', views.excluir_tarefas_usuario, name='excluir_tarefas_usuario'),
    path('editar_tarefa/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
]