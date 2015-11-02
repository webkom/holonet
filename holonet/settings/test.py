TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'NAME': 'holonet'
    }
}

BROKER_URL = 'redis://127.0.0.1'

REDIS = {
    'host': '127.0.0.1',
}

ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}
