TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'NAME': 'holonet'
    }
}
