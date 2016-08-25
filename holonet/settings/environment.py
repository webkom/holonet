import environ

root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db()
}

CACHES = {
    'default': env.cache(),
}

SECRET_KEY = env('SECRET_KEY')
