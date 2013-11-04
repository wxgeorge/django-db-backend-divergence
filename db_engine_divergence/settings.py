MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'divergence_test',
        'USER': 'django',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',                      
    }
}

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': '/tmp/sqlite',    
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DATABASES=SQLITE
USE_TZ=True

# immaterial for this example, but manage.py won't run without it.
SECRET_KEY = 'fcmz(=^=9wjk(2lr*_^wvu2sy&0)h7xa5ck%0tea43-vc6n%pt'

INSTALLED_APPS = (
  'example_app'
)
