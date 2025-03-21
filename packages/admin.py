from django.contrib import admin
from .models import *

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing TravelPackage models. Provides functionalities to display essential fields and search by package name, destination, and associated tag names.
Claro! Aqui está a tradução para o português:

Interface administrativa para gerenciar modelos de TravelPackage. Fornece funcionalidades para exibir campos essenciais e buscar por nome do pacote, destino e nomes das tags associadas.
    """
    list_display = ('name', 'destination', 'price', 'rating', 'available', 'duration')
    search_fields = ('name', 'destination', 'tags__name')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Interface administrativa para gerenciar modelos de Tag. Permite a visualização e busca de tags por nome.
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
   Interface administrativa para gerenciar modelos de Reserva. Permite a visualização, busca e filtragem de dados de reserva, incluindo pacote, status de pagamento e método de pagamento.
    """
    list_display = ('name', 'email', 'num_adults', 'num_children', 'payment_method', 'payment_status', 'total_price', 'datetime', 'package')
    search_fields = ('name', 'email', 'package__name')
    list_filter = ('payment_status', 'payment_method', 'package')



@admin.register(Citys)

class CitysAdmin(admin.ModelAdmin): 
    """
    Interface administrativa para gerenciar modelos de Cidade. Permite a visualização, busca e filtragem de dados de cidades, incluindo nome e país.
    """
    search_fields = ['name']
@admin.register(Hoteis)
class HoteisAdmin(admin.ModelAdmin):
    """
    Interface administrativa para gerenciar modelos de Hotel. Permite a visualização, busca e filtragem de dados de hotéis, incluindo nome, endereço, classificação e disponibilidade.
    """
    list_display = ('name','city')
@admin.register(HotelTarifa)
class HotelTarifaAdmin(admin.ModelAdmin):
    """
    Interface administrativa para gerenciar modelos de Tarifa de Hotel. Permite a visualização, busca e filtragem de dados de tarifas de hotéis, incluindo hotel, diária, adulto, criança, data de início e fim.
    """
    list_display = ('hotel', 'start_date', 'end_date')
    search_fields=('hotel','start_date', 'end_date')
    
    list_filter = ('hotel', 'start_date', 'end_date')
    ordering = ('hotel', 'start_date', 'end_date')
