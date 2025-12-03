from django.contrib import admin #type: ignore

# Register your models here.

from .models import ITSM_Ticket_Model, ITSM_Role_Model, ITSM_User_Model, ITSM_Group_Model

@admin.register(ITSM_Ticket_Model)
class TicketAdmin(admin.ModelAdmin):
   pass

@admin.register(ITSM_Role_Model)
class RoleAdmin(admin.ModelAdmin):
   list_per_page = 10
   search_fields = ('id', 'name', )
   list_display = ('id', 'name', 'name_ger', )
   ordering = ('id', )
   list_editable = ('name_ger', )
   list_filter = ('name_ger', )
   

@admin.register(ITSM_User_Model)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'first_name', 'last_name', 'email', )
    list_per_page = 10
    search_fields = ('id', 'name', 'first_name', 'last_name', 'email', )
    list_filter = ('role', )
    ordering = ('id', )
    list_editable = ('role', )
    list_display_links = ('name',)
    

@admin.register(ITSM_Group_Model)
class GroupAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'descricao', )
   list_per_page = 10
   

