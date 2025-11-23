from django.db import models
from django.contrib.auth.models import User, Group

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
    descricao = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
class ITSM_User_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    role = models.ForeignKey(ITSM_Role_Model, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} | {self.role.name}'
    
    def save(self):
        self.name = self.name.title()
        self.email = self.email.lower()
        super(ITSM_User_Model, self).save()
    
class ITSM_Group_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descricao = models.TextField()
    membros = models.ManyToManyField(ITSM_User_Model)

    def __str__(self):
        return f'{self.name} | Membros: {self.membros.count()}'
    
    def save(self):
        self.name = self.name.title()
        super(ITSM_Group_Model, self).save()