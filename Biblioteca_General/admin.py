from django.contrib import admin
from .models import Biblioteca, Autor, Libro, Cliente, DatosClientes

# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(DatosClientes)