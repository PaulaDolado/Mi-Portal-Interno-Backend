# mi_backend/settings.py
import os
from pathlib import Path

DEBUG = True 
ROOT_URLCONF = 'config.urls'
STATIC_URL = 'static/' 
SECRET_KEY = 'ClaveUltraMegaSecreta'

INSTALLED_APPS = [
    # APPS ESENCIALES DE DJANGO (¡Deben estar aquí!)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # TERCEROS
    'corsheaders', 
    'rest_framework',

    # TU APLICACIÓN
    'api',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Permitir peticiones de frontend
CORS_ALLOWED_ORIGINS = [ #->CAMBIAR EN PROD.!!
    "http://localhost:5173",  # Vite
    "http://127.0.0.1:5173",
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
]

# Configuraciones adicionales
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

BASE_DIR = Path(__file__).resolve().parent.parent #raíz del proy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        #ruta donde se guardará el archivo bbdd
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}
