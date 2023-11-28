from django.contrib import admin
from .models import Usuarios
from .models import Camisas
from .models import Sudaderas
from .models import Pantalones
from .models import Tenis
from .models import Carrito



# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Carrito)
admin.site.register(Camisas)
admin.site.register(Sudaderas)
admin.site.register(Pantalones)
admin.site.register(Tenis)










