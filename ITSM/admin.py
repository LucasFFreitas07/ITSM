from django.contrib import admin

# Register your models here.

from .models import ITSM_Ticket_Model, ITSM_Role_Model, ITSM_User_Model, ITSM_Group_Model

@admin.register(ITSM_Ticket_Model)
class TicketAdmin(admin.ModelAdmin):
   pass

@admin.register(ITSM_Role_Model)
class RoleAdmin(admin.ModelAdmin):
   list_per_page = 10
   search_fields = ('id', 'name', )
   

@admin.register(ITSM_User_Model)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', )
    list_per_page = 10
    search_fields = ('id', 'name', )
    list_filter = ('role', )
    ordering = ('id', )
    list_editable = ('role', )
    

@admin.register(ITSM_Group_Model)
class GroupAdmin(admin.ModelAdmin):
   pass
   

