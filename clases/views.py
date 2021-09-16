# Create your views here.
import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from clases.models import User


class PaginaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id, contra):
        if id != '':
            usuarios = list(User.objects.filter(cnickname=id, password=contra).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': 'Success', 'usuario': usuario}
            else:
                datos = {'message': 'Usuario no encontrado'}
            return JsonResponse(datos)
        else:
            usuarios = list(User.objects.values())
            if len(usuarios) > 0:
                datos = {'message': 'Success', 'usuarios': usuarios}
            else:
                datos = {'message': 'Usuarios no encontrados'}
            return JsonResponse(datos)
    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        print(jd)
        User.objects.create(**jd)
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios = list(User.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario = User.objects.get(id=id)

        else:
            datos = {'message': 'Usuario no encontrado'}

    def delete(self, request):
        pass
