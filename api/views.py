# Mi-Portal-Interno-Backend/api/views.py

from rest_framework import viewsets
from .models import Empleado       
from .serializers import EmpleadoSerializer 

class EmpleadoViewSet(viewsets.ModelViewSet): 
    """
    Proporciona los métodos CRUD para el modelo Empleado.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer