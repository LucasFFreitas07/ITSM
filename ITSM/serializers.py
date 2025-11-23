from django.contrib.auth.models import User, Group
from django.db import *
from rest_framework import serializers
from .models import ITSM_Ticket_Model, ITSM_User_Model, ITSM_Role_Model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups',]
        # fields = '__all__'
        # fields = ['id', 'username', 'email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class ITSM_Ticket_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_Ticket_Model
        fields = '__all__'

class ITSM_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_User_Model
        fields = '__all__'

class ITSM_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_Role_Model
        fields = '__all__'