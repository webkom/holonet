MASTER_DOMAINS = [
    'test.holonet.no'
]

TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

SENDER_WHITELIST_ENABLED = False
DOMAIN_WHITELIST_ENABLED = False

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'NAME': 'hansolo'
    }
}
