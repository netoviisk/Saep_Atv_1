from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_tarefa/', views.cadastro_tarefa, name='cadastro_tarefa'),
]
