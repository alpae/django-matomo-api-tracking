import os

SECRET_KEY = 'foo'
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'matomo_api_tracking',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

STATIC_URL = ''
MATOMO_API_TRACKING = {
        'url': 'https://your-matomo-server.com/',
        'site_id': 1,
        # 'ignore_paths': ["/debug/", "/health/"],
    }

CUSTOM_UIP_HEADER = 'HTTP_X_IORG_FBS_UIP'

TEST_RUNNER = 'matomo_api_tracking.test_runner.CeleryTestSuiteRunner'

CELERY_ALWAYS_EAGER = True
