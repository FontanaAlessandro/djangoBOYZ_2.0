from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Chat
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from django.shortcuts import render


@login_required(login_url="/admin/")
def chat_list(request, user_pk=None):
    users = User.objects.all()
    if request.user.is_authenticated == False:
        # TODO 
        raise Http404
    whoami = request.user
    if user_pk == None:
        ''' TODO Fai Welcome Message '''
        chat_obj = None
    else:
        user_obj = User.objects.get(id=user_pk)
        query_chat = Q(user1=user_obj, user2=whoami) | Q(user1=whoami, user2=user_obj)
        chat_qset = Chat.objects.filter(query_chat)        
        if chat_qset.count() > 1:
            raise ValueError('E\' successo un casino')
        elif chat_qset.count() == 0:
            chat_obj = Chat(user1=whoami, user2=user_obj)
            chat_obj.save()
        else:
            chat_obj = chat_qset.first()
    
    return render(request, 'blog/post_list.html',
                   {'chat': chat_obj,
                    'users':users,
                    'whoami': whoami})


@login_required(login_url="/admin/")
def chat_room(request, room):
    return render(request, 'blog/room.html', {'nome':room})                           

def api_get_users(request):
    context_json = {}
    context_json['status'] = 'success'
    context_json['msg'] = 'abbiamo recuperato un messaggio '
    context_json['users'] = []
    for u in User.objects.all():
        context_json['users'].append({'first_name': u.first_name, 'last_name': u.last_name })
    json_data= json.dumps(context_json)
    return HttpResponse(json_data, content_type='application/json')


def api_get_message(request):
    context_json = {}
    context_json['messaggi'] = []
    for u in User.objects.all():
        context_json['users'].append({'first_name': u.first_name, 'last_name': u.last_name })
    json_data= json.dumps(context_json)
    return  HttpResponse(json_data, content_type='application/json')



messaggi = [] 

def api_get_message(request):
    return HttpResponse({'messaggi': messaggi})

def riceviMessaggio(request):
    if request.method == 'POST':
        dati = json.loads(request.body)
        messaggio = dati.get('messaggio')
        print('Messaggio ricevuto:', messaggio)

        messaggi.append(messaggio)

        return HttpResponse({'success': True})
    else:
        return HttpResponse({'success': False, 'error': 'Metodo non consentito'})
    
def index(request):
     return render(request, "blog/post_list.html")
     

