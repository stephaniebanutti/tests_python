from django.shortcuts import render
from animais.models import Animal

def index(request):
    context = {'caracteristicas': None}
    if 'buscar' in request.GET:
        animais = Animal.objects.all()
        animal_pesquisando = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains = animal_pesquisando)
        context = {'caracteristicas' : caracteristicas}
    return render(request, 'index.html', context)