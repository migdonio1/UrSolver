from django.contrib import admin

from .models import Solvers, Skill

class ChoiceInline(admin.TabularInline):
    model = Skill
    extra = 3


class SolverAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Username']}),
        ('Informacion de Fecha', {'fields': ['fechaRegistro']}),
        ('Datos Solver', {'fields': ('Email','Name','Age','password')})
    ]
    inlines = [ChoiceInline]
    list_display = ('Username','password','fechaRegistro', 'Email', 'Name', 'Age')
    list_filter = ['fechaRegistro']
    search_fields = ['Username']
admin.site.register(Solvers, SolverAdmin)