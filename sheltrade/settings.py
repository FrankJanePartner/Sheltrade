import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Set up environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')

# API and other important info
VTPass_API_KEY=env('VTPass_API_KEY')
VTPass_PUBLIC_KEY=env('VTPass_PUBLIC_KEY')
VTPass_SECRET_KEY=env('VTPass_SECRET_KEY')
VTPass_BASE_URL=env('VTPass_BASE_URL')
VTPass_EMAIL=env('VTPass_EMAIL')  # Replace with your Vtpass email
VTPass_PASSWORD=env('VTPass_PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []#'sheltrade.godhouse.org', 'https://www.sheltrade.godhouse.org', 'www.sheltrade.godhouse.org', 'sheltrade.pythonanywhere.com', 'https://www.sheltrade.pythonanywhere.com', 'www.sheltrade.pythonanywhere.com']



SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.humanize",
    
    # my apps
    'contact',
    'core',
    'crypto',
    'giftcard',
    'wallet',
    'mobileTopUp',
    'billPayments',
    'sheltradeAdmin',

    # third-party apps
    # 'djmoney',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # allauth specific middleware
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'sheltrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "core.context_processors.currency",
                "core.context_processors.UserProfile",
                "sheltradeAdmin.context_processors.details",
                # "django.core.context_processors.request",
                # 'allauth.account.context_processors.account',
                # "allauth.socialaccount.context_processors.socialaccount",

            ],
        },
    },
]

WSGI_APPLICATION = 'sheltrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS= [BASE_DIR / 'static']
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'  # Add a leading slash for correct URL path
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'



SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ]
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': '74765500020-gi7u5q1nmani6kemv428ckn936k4bncd.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'APP': {
            'client_id': '509697181767177',
            'secret': '651a9335cb086c9c8d5fca07d71f1a86',
            'key': ''
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 465 if using SSL
EMAIL_USE_TLS = True  # Change to False if using SSL (port 465)
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'myappsa9@gmail.com'
EMAIL_HOST_PASSWORD = 'nrgh zjca vijp fkbl'
DEFAULT_FROM_EMAIL = 'partnermarvel55@gmail.com'



LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


# ACCOUNT_EMAIL_VERIFICATION = 'none'  # Disable email verification
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True  # Redirect users after login
