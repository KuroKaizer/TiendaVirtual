from config.wsgi import *

# Create your tests here.

from core.erp.models import Type

# Listar

# query = Type.objects.all()
# print(query)

# Inserccion
# t = Type(name="Secretario").save()
# t.name = 'Presidente'

# Editar
# try:
#     t = Type.objects.get(pk=3)
#     t.name = "Gerente"
#     t.save()
# except Exception as e:
#     print(e)

# # Eliminacion
# t = Type.objects.get(pk=3)
# t.delete()
