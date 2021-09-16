from django.urls import path

from clases.views import PaginaView

urlpatterns = [
    path('users/', PaginaView.as_view(), name='usuarios_list'),
    #path('users/<int:id>', PaginaView.as_view(), name='usuarios_proceso'),
    path('users/<str:id>;<str:contra>', PaginaView.as_view(), name='usuarios_process')
]