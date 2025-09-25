from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet 

# Crea un router que genera automáticamente las rutas CRUD (GET, POST, PUT, DELETE)
router = DefaultRouter()

# Registra tu ViewSet de Empleado bajo el prefijo 'empleados'. 
# Esto crea rutas como: /api/empleados/ y /api/empleados/{pk}/
router.register(r'empleados', EmpleadoViewSet, basename='empleado') 

# El patrón de URLs final son las rutas que el router ha generado
urlpatterns = router.urls