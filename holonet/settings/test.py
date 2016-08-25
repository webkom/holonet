SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'holonet',
        'USER': 'holonet',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

BROKER_URL = 'redis://127.0.0.1'

ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}
