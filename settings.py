# mi_backend/settings.py
INSTALLED_APPS = [
    # ...
    'corsheaders',  # AGREGAR AQUÍ
    'rest_framework',
    'api',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    # ... el resto de la lista ...
]

# Permitir peticiones desde tu puerto de desarrollo de frontend
#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:3000",
#    "http://127.0.0.1:3000",
#]

# O si quieres permitir TODAS las peticiones (NO recomendado para producción, solo para desarrollo rápido)
CORS_ALLOW_ALL_ORIGINS = True