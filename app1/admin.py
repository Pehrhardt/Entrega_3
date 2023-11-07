from django.contrib import admin
from app1.models import Cliente, fondos, bonos, acciones

# Register your models here.

admin.site.register(Cliente)
admin.site.register(fondos)
admin.site.register(bonos)
admin.site.register(acciones)
