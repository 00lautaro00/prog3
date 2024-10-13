from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estudiante/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiante/mayores_de/', views.listar_por_parametro, name ='listar_por_parametro'),
    path('curso/', views.listar_cursos, name='listar_curso'),
    path('curso/<int:id>/', views.findOneCurso, name = 'curso')
] 
