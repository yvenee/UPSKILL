from datetime import datetime, timedelta, timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse


# Create your views here.

#@login_required() # Só acessa a página se estiver logado 
@login_required(login_url='/login/') # Só acessa a página se estiver logado e se não tiver logado, redireciona para página de login
def event_list(request):
    #
    #### Filtros ####
    
    # Por um determinado atributo
    # event = Event.objects.get(id=1) # lista apenas o id=1
    # data = {'event' : event} # 'event' é a chave que será usada no html para acessar os valores
    
    # Por usuário
    user = request.user
    now = datetime.now() - timedelta(hours=1)
    #event = Event.objects.filter(user=user) # lista todos os eventos do usuario que está logado
    event = Event.objects.filter(user=user, event_date__gt=now, active=True) # lista todos os eventos do usuario que está logado e que a data do evento seja superior a data/hora atual - 1 hora
    # NOTA: __gt para >= __lt para <=  
    data = {'events' : event} # 'events' é a chave que será usada no html para acessar os valores

    # Listar todos
    # event = Event.objects.all # lista todos
    # data = {'events' : event} # 'events' é a chave que será usada no html para acessar os valores
    return render(request, 'schedule.html', data)

@login_required(login_url='/login/')
def event(request):
    # Para fazer o edit
    event_id = request.GET.get('id')
    data = {}
    if event_id:
        data['event']= Event.objects.get(id=event_id)
    # ------ fim ------
    return render(request, 'event.html', data)

@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title') # title é o nome do input na view         
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        event_id = request.POST.get('event_id')
        # 1ª forma para o edit com validação do usuário -----
        if event_id:
            event = Event.objects.get(id=event_id)
            if event.user == user:
                event.title = title
                event.event_date = event_date
                event.description = description
                event.active = True
                event.save()
        # 2ª forma para o edit -----
        # if event_id:
        #     Event.objects.filter(id=event_id).update(title=title,
        #                                                event_date=event_date,
        #                                                description=description)
        # # --- fim -----
        else:
            Event.objects.create(title=title,
                             event_date=event_date,
                             description=description,
                             user=user, active=True)

        return redirect('/')

""" Forma de redirecionar uma url para uma outra url 
def index(resquest):
    return redirect('/agenda/') """

def login_user(request):
    return render(request, 'login.html')

def logout_user(resquest):
    logout(resquest)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # autentica o usuário
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'User or password invalid!')
    return redirect('/')

# FUNÇÃO SEM USO NESTE MOMENTO POIS OPTOU-SE POR FAZER UMA ROTINA QUE DELETA O EVENTO QUE ESTÁ INATIVO HÁ MAIS DE 2 MESES #
@login_required(login_url='/login/')
def delete_event(request, event_id):
    user = request.user

    try:
        event = Event.objects.get(id=event_id) # procura o evento do id informado
    except:
        raise Http404()
    
    if user == event.user: # compara se o usuário logado é o dono do evento encontrado
        event.active = False 
        event.save()
        # event.delete() # deleta direto na base de dados
    else:
        raise Http404()

    # Aqui é uma forma de fazer o delete mas não tem a validação, então qualquer pessoa pode excluir eventos de outras pessoas.
    # src_event = Event.objects.filter(id=event_id)
    # src_event.delete()
    return redirect('/')

# ----- FIM ----- #

@login_required(login_url='/login/')
def jason_event_list(request):
    user = request.user
    event = Event.objects.filter(user=user).values('id', 'title')
    return JsonResponse(list(event), safe=False) #usa o safe pq está passando uma lista

@login_required(login_url='/login/')
def event_history(request):
    user = request.user
    two_months_ago = datetime.now() - timedelta(weeks=8)
    event = Event.objects.filter(user=user, event_date__lte=datetime.now(), event_date__gte=two_months_ago).order_by('-create_date') # ordena de forma descrescente pela data de criação
    data = {'events' : event}
    return render(request, 'history.html', data)

