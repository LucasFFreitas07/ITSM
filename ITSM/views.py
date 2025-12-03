from django.http import HttpResponse #type: ignore
from django.shortcuts import render #type: ignore
from rest_framework import viewsets #type: ignore
from .models import ITSM_Ticket_Model, ITSM_User_Model, ITSM_Group_Model
from .serializers import ITSM_Ticket_Serializer, ITSM_User_Serializer, ITSM_Group_Serializer
from drf_spectacular.utils import extend_schema, extend_schema_view #type: ignore
from django.template import loader #type: ignore
from .forms import PasswordResetForm, UserForm

# Create your views here.
@extend_schema_view(
    list=extend_schema(
        description="Retorna a lista de todos os usuários.",
    ),
    retrieve=extend_schema(
        description="Retorna os detalhes de um usuário específico por ID.",
    ),
    create=extend_schema(
        description="Cria um novo usuário.",
        parameters=[
            {
                "name": "username",
                "description": "Nome de usuário do novo usuário.",
                "required": True,
                "type": "string",
            },
            {
                "name": "first_name",
                "description": "Primeiro nome do novo usuário.",
                "required": False,
                "type": "string",
            },
            {
                "name": "last_name",
                "description": "Sobrenome do novo usuário.",
                "required": False,
                "type": "string",
            },
            {
                "name": "email",
                "description": "Email do novo usuário.",
                "required": False,
                "type": "string",
            },
        ]
    ),
    update=extend_schema(
        description="Atualiza um usuário existente por ID.",
        parameters=[
            {
                "name": "username",
                "description": "Nome de usuário do usuário.",
                "required": True,
                "type": "string",
            },
            {
                "name": "first_name",
                "description": "Primeiro nome do usuário.",
                "required": False,
                "type": "string",
            },
            {
                "name": "last_name",
                "description": "Sobrenome do usuário.",
                "required": False,
                "type": "string",
            },
            {
                "name": "email",
                "description": "Email do usuário.",
                "required": False,
                "type": "string",
            },
        ]
    ),
    partial_update=extend_schema(
        description="Atualiza parcialmente um usuário existente por ID.",
    ),
    destroy=extend_schema(
        description="Exclui um usuário existente por ID.",
    )
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = ITSM_User_Model.objects.all()
    serializer_class = ITSM_User_Serializer

@extend_schema_view(
    list=extend_schema(
        description="Retorna a lista de todos os grupos.",
    ),
    retrieve=extend_schema(
        description="Retorna os detalhes de um grupo específico por ID.",
    ),
    create=extend_schema(
        description="Cria um novo grupo.",
        parameters=[
            {
                "name": "name",
                "description": "Nome do novo grupo.",
                "required": True,
                "type": "string",
            },
        ]
    ),
    update=extend_schema(
        description="Atualiza um grupo existente por ID.",
        parameters=[
            {
                "name": "name",
                "description": "Nome do grupo.",
                "required": True,
                "type": "string",
            },
        ]
    ),
    partial_update=extend_schema(
        description="Atualiza parcialmente um grupo existente por ID.",
    ),
    destroy=extend_schema(
        description="Exclui um grupo existente por ID.",
    
    )
    )
class GroupViewSet(viewsets.ModelViewSet):
    queryset = ITSM_Group_Model.objects.all()
    serializer_class = ITSM_Group_Serializer


class ITSM_Ticket_ViewSet(viewsets.ModelViewSet):
    queryset = ITSM_Ticket_Model.objects.all()
    serializer_class = ITSM_Ticket_Serializer

def index(request):
    return render(request, 'partials/menu.html')

def users(request):
    users = ITSM_User_Model.objects.all().order_by('name')
    role = ITSM_Group_Model.objects.all()
    template = loader.get_template('users.html')
    context = {
        'users': users,
        'role': role
    }
    return HttpResponse(template.render(context, request))

def pass_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Senha redefinida com sucesso.")
    return render(request, 'password_reset.html', {'form': PasswordResetForm()})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuário criado com sucesso.")
    return render(request, 'create_user.html', {'form': UserForm()})
    