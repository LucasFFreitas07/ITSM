from django.db import models #type: ignore
from django.contrib.auth.models import User, Group #type: ignore
from django.core.exceptions import ValidationError #type: ignore


# Create your models here.
class ITSM_Ticket_Model(models.Model):

    STATUS_CHOICES = [
        ('Open', 'Aberto'),
        ('In Progress', 'Em Progresso'),
        ('Resolved', 'Resolvido'),
        ('Closed', 'Fechado'),
    ]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aberto = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Open', choices=STATUS_CHOICES)

    def __str__(self):
        number_format = f'SD{self.id}'
        return f'Chamado: {number_format} | Título: {self.titulo} | Status: {self.status}'
    
class ITSM_Role_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_ger = models.ForeignKey('ITSM_User_Model', on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.name = self.name
        self.descricao = self.descricao
        role = ITSM_Role_Model.objects.filter(name=self.name).exclude(pk=self.pk).first()
        if role:
            raise ValidationError("Grupo já existe.")
        
        super(ITSM_Role_Model, self).save(*args, **kwargs)
        
class ITSM_User_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    role = models.ForeignKey(ITSM_Role_Model, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.first_name = self.first_name.title() if self.first_name else ''
        self.last_name = self.last_name.title() if self.last_name else ''
        self.email = self.email.lower()
        self.senha = self.senha        

        existing_name = ITSM_User_Model.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists()
        if existing_name:
            raise ValidationError({'name': 'Nome de usuário já existe.'})

        existing_email = ITSM_User_Model.objects.filter(email__iexact=self.email).exclude(pk=self.pk).exists()
        if existing_email:
            raise ValidationError({'email': 'Email já cadastrado.'})

        super(ITSM_User_Model, self).save(*args, **kwargs)

    
class ITSM_Group_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descricao = models.TextField()
    membros = models.ManyToManyField(ITSM_User_Model)

    def __str__(self):
        return f'{self.name} | Membros: {self.membros.count()}'
    
    def save(self, *args, **kwargs):
        self.name = self.name
        super(ITSM_Group_Model, self).save(*args, **kwargs)