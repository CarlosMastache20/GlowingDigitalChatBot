from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random
import re 
from .models import Info
from .forms import createInfo, personaEcargada
from .utils import * 
from django.http.response import JsonResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.



# bot = ChatBot('chatbot', read_only = False, logic_adapters=[{
    
    
#     'import_path' : 'chatterbot.logic.BestMatch',
    
#     'default_response': 'Lo siento, no entendi tu pregunta. Puedas intera usando otras palabras por favor',
#     'maximun_similarity_threshold':0.90
    
#     }])

# list_to_train = [

#     "hola",#question
#     "Hola, en que podemos ayudar",#answer
#     "informacion",
#     "Somos una empresa de marketing",
#     "es real todo esto",
#     "Si, es real todo esto"
# ]

#chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

#chatterbotCorpusTrainer.train('chatterbot.corpus.spanish')

def index(request):
    return render(request, 'blog/index.html')

def inicio(request):
    return render(request, 'blog/inicio.html')

def nosotros(request):
    return render(request, 'blog/nosotros.html')

def contacto(request):
    return render(request, 'blog/contactanos.html')

def testimonios(request):
    return render(request, 'blog/testimonios.html')

def paginas(request):
    return render(request, 'blog/nuestraspaginas.html')
    
def modal(request):
    return render(request, 'blog/modal.html')


@login_required
def registrarUsuarios(request):
    if request.method == 'GET':
         return render(request, 'blog/signup.html' , {
        'form' : UserCreationForm
        })

    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                messages.success(request, 'Nuevo Administrador Guardado Correctamente')
                return redirect('obtenerinfo')
            except IntegrityError:
                 return render(request, 'blog/signup.html' , {
                 'form' : UserCreationForm,
                 "error" :"Usario ya existe"
                })
        return render(request, 'blog/signup.html' , {
                 'form' : UserCreationForm,
                 "error" :"Las contraseñas no coinciden"
                })

def signin(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html' , {
            'form' : AuthenticationForm
        }) 
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request, 'blog/login.html' , {
            'form' : AuthenticationForm,
            'error' : 'Usuario o contraseña incorrecto'
            })
        else: 
            login(request, user)
            return redirect('obtenerinfo')



#def getResponse(request):
   # userMessage = request.GET.get('userMessage')
    #chatResponse = str(bot.get_response(userMessage))
    #return HttpResponse(chatResponse)


def getResponse(request):

    split_message = re.split(r'\s|[,:;.?-_]\s*', normalize(request.GET.get('userMessage').lower()))
    response = check_all_messages(split_message)
    return HttpResponse(response)

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def create_info(request):

    if request.method == 'GET':
        return render(request, 'blog/contactanos.html' ,{
        'form' : createInfo 
        })
    else:
        form = createInfo(request.POST)
        newInfo = form.save(commit=False)
        newInfo.date = timezone.now()
        newInfo.save()
        messages.success(request, 'Datos Enviados correctamente')
        return redirect('contacto')  

        #return render(request, 'blog/contactanos.html',{
        #    'form' : createInfo,
        #    'guardado': 'datos enviados correctamente' 
        #})

def create_infoBot(request):
    form = createInfo(request.POST)
    newInfo = form.save(commit=False)
    newInfo.date = timezone.now()
    newInfo.save()
    messages.success(request, 'Tu registro ya esta hecho')
    return redirect('inicio')  



@login_required
def AllInfo(request):
   # infos = list( Info.objects.values().filter(contactado=False))
    #data = {'infos' : infos}
    #return JsonResponse(data)

    infos=Info.objects.filter(contactado=False, tEncargado=None)
    return render(request, 'blog/info.html', {
        'infos':infos
    })

@login_required
def AllInfoContacted(request):
    infos=Info.objects.filter(contactado=True)
    return render(request, 'blog/infoContacted.html', {
        'infos':infos
    })    

@login_required
def contacted(request, info_id):
    info= get_object_or_404(Info, pk=info_id )
    if request.method == 'POST':
        form = personaEcargada(request.POST, instance=info)
        form.save()
        messages.success(request, 'Persona Marcada como contactada')
        return redirect('obtenerinfo')  

@login_required
def eliminar(request, info_id):
    info= get_object_or_404(Info, pk=info_id )
    if request.method == 'POST':
        info.delete()
        messages.success(request, 'Persona Eliminada')
        return redirect('contacted')  

#def viewAdmin(request):
 #   return render(request, 'blog/info.html')
@login_required
def salir(request): 
    logout(request)
    return redirect('inicio')