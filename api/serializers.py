# Mi-Portal-Interno-Backend/api/serializers.py
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__' # incluirá nuevos campos auto