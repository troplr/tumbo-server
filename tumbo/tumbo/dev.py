from settings import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
#REDIS_URL = "redis://127.0.0.1:6379/1"
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#SESSION_CACHE_ALIAS = "default"
#CACHES = {
#    "default": {
#        "BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": REDIS_URL,
#        "OPTIONS": {
#            "CLIENT_CLASS": "django_redis.client.DefaultClient",
#            }
#    }
#}

STATIC_URL = '/static/'

RABBITMQ_HTTP_API_PORT = "15672"
RABBITMQ_ADMIN_USER = "guest"
RABBITMQ_ADMIN_PASSWORD = "guest"
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672

DROPBOX_CONSUMER_KEY = os.environ['DROPBOX_CONSUMER_KEY']
DROPBOX_CONSUMER_SECRET = os.environ['DROPBOX_CONSUMER_SECRET']
DROPBOX_REDIRECT_URL = os.environ['DROPBOX_REDIRECT_URL']

# Spawn
FASTAPP_WORKER_IMPLEMENTATION = "core.executors.worker_engines.spawnproc.SpawnExecutor"

# Rancher
#FASTAPP_WORKER_IMPLEMENTATION = "core.executors.worker_engines.rancher.RancherApiExecutor"
RANCHER_ACCESS_KEY="0F91E6F0567CB4006008"
RANCHER_ACCESS_SECRET="8jHYKwWw5RSE72fGGvEF8UgbmtXLj62BzGKZwRvJ"
RANCHER_ENVIRONMENT_ID="1e1"
RANCHER_URL="http://192.168.99.1:8080"


FASTAPP_CORE_SENDER_PASSWORD = "h8h9h0h1h2h3"
FASTAPP_CORE_RECEIVER_PASSWORD = "h8h9h0h1h2h3"

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = "/static/"

DEBUG = True
# TODO: get from var
#WORKER_RABBITMQ_HOST = "192.168.99.1"
WORKER_RABBITMQ_HOST = "localhost"
WORKER_RABBITMQ_PORT = "5672"
ALLOWED_HOSTS = "*"

FASTAPP_REPOSITORIES_PATH = "/home/philipsahli/workspace"
FASTAPP_DEV_STORAGE_DROPBOX_PATH = "/home/philipsahli/Dropbox/Apps/tumbo dev/"

FASTAPP_PLUGINS_CONFIG = {
    'core.plugins.stats': {},
    'core.plugins.rabbitmq': {},
    'core.plugins.dnsname': {
        'provider': "DigitalOcean",
        'token': os.environ.get('DIGITALOCEAN_CONFIG', None),
        'zone': "hosts-dev.planet-lite-test.sahli.net"
    },
    'core.plugins.datastore': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        #'HOST': "192.168.99.1",
        'HOST': "127.0.0.1",
        'PORT': "15432",
        'NAME': "store",
        'USER': "store",
        'PASSWORD': "store123"
    }
}

if "TUTUM_SERVICE_API_URI" in os.environ:
    FASTAPP_PLUGINS_CONFIG.update(
        {
            'core.plugins.tutumlogs': {}
        }
    )

FASTAPP_SCHEDULE_JOBSTORE = "sqlite:////tmp/jobstore.db"

REDIS_METRICS['PASSWORD'] = os.environ.get('CACHE_ENV_REDIS_PASS', None)

TEMPLATE_LOADERS += (
     'core.loader.DevLocalRepositoryPathLoader',
)