"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import config
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x7ciez#kn3j2-a^efc)zi3jj-1g@2_2lg_w2y_2^hgmq9b8k3='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # DEBUG 대신 INFO로 변경
            'propagate': True,
        },
        'your_app_name': {  # 여기에서 app 이름을 사용하세요.
            'handlers': ['console'],
            'level': 'INFO',  # DEBUG 대신 INFO로 변경
            'propagate': True,
        },
    },
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB (10 * 1024 * 1024)

MEDIA_URL = '/media/'  # URL 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 실제 파일이 저장되는 경로

# media 디렉토리 내의 recordings 폴더가 존재하는지 확인하거나 자동으로 생성
os.makedirs(os.path.join(MEDIA_ROOT, 'recordings'), exist_ok=True)

ALLOWED_HOSTS = []
# KAKAO API 설정
KAKAO_API_KEY='171d35b8550f9fd896fe5f3724668e0d'
KAKAO_API_URL='https://dapi.kakao.com/v2/local/search/keyword.json'  # 실제 카카오 API URL로 변경

KAKAO_SDK_API_KEY='8371fd535d5d33dfcec6e7f3cdce0d5a'

# 공공데이터 API 설정
PUBLIC_DATA_API_KEY='k3j+rBdCFRKV+wyerVxM7H2jyevfSU3PYoLwzcO62WXtbD0osGwAVNJYCXMphlfjoPofM/5VR7JDg8IabF8zOg=='
PUBLIC_DATA_API_URL='http://apis.data.go.kr/B552474/SenuriService/getJobList'  # 실제 공공데이터 API URL로 변경
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'app',
    'accounts',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # 프로젝트 템플릿 경로 추가
            BASE_DIR / 'accounts/templates',  # accounts 앱의 템플릿 경로 추가
            BASE_DIR / 'app/templates',  # app의 템플릿 경로
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'search_history_db': {  # 검색 기록을 위한 별도의 데이터베이스
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'search_history_db.sqlite3',  # 검색 기록용 데이터베이스
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# C:\go\site\config\settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
