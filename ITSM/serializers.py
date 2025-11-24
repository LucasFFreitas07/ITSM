from django.db import * #type: ignore
from rest_framework import serializers #type: ignore
from .models import ITSM_Ticket_Model, ITSM_User_Model, ITSM_Role_Model, ITSM_Group_Model



class ITSM_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_Group_Model
        fields = ['id', 'name']

class ITSM_Ticket_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_Ticket_Model
        fields = '__all__'

class ITSM_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_User_Model
        exclude = ['senha', 'role',]
        # fields = '__all__'

class ITSM_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ITSM_Role_Model
        fields = '__all__'