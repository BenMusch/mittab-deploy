import os


class BaseConfig(object):
    WEB_CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG'] == 'True'

    DB_FILE = 'db.sqlite'
    DB_PATH = os.path.join(os.path.abspath(os.path.dirname(DB_FILE)), DB_FILE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 120

    # configure celery to work with sqs
    # AWS creds auto-loaded from AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY env
    # vars
    CELERY_RESULT_BACKEND = None
    CELERY_BROKER_URL = 'sqs://'
    SQS_QUEUE_NAME = os.environ['SQS_QUEUE']
    CELERY_DEFAULT_QUEUE = SQS_QUEUE_NAME

    # for Flask-Webhooks extension
    GITHUB_WEBHOOKS_KEY = os.environ['GITHUB_SECRET']
    VALIDATE_IP = False
    VALIDATE_SIGNATURE = True

    # for Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['benmuschol@gmail.com']

    # DigitalOcean server config
    # https://developers.digitalocean.com/documentation/changelog/api-v2/new-size-slugs-for-droplet-plan-changes/
    DEFAULT_SIZE_SLUG = 's-1vcpu-2gb'
    TEST_SIZE_SLUG = 's-1vcpu-1gb'
