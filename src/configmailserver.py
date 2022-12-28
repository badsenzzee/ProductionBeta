# mailserver_config.py
import os
from website_app.debug_services.debug_log_services import *

log_config_start(__file__, 'mailserver_configuration')

MAIL_SERVER_PROVIDER = os.environ.get('MAIL_SERVER_PROVIDER', 'GOOGLE')
log_variable('MAIL_SERVER_PROVIDER', MAIL_SERVER_PROVIDER)

################################################################
### mail servers
################################################################
GREENJET_MAIL_SERVER = 'in-ver3.greenanimalsbank.com'
GREENJET_MAIL_PORT = '587' # Port 25 or 587 (some providers block port 25). If TLS on port 587 doesn't work, try using port 465 and/or using SSL instead
GREENJET_MAIL_USE_TLS = 'True'
GREENJET_MAIL_USE_SSL = 'True'
GREENJET_MAIL_USERNAME = 'a98733207c3c7b3358f2f74e809a11946'
GREENJET_MAIL_PASSWORD = '3a6a2c2de4144bca2435382f3e216739'
GREENJET_MAIL_APIKEY_PUBLIC ='c3c33bca2437a1ecaf2f782f3e257786'
GREENJET_MAIL_APIKEY_PRIVATE ='98733c2de41ff2167395382f3e2bca24'

YANDEX_MAIL_SERVER = "smtp.yandex.ru"
YANDEX_MAIL_PORT = '587'
YANDEX_MAIL_USE_TLS = 'True'
YANDEX_MAIL_USE_SSL = 'True'
YANDEX_MAIL_USERNAME = '...' #without the @yandex.ru
YANDEX_MAIL_PASSWORD = '***'
YANDEX_MAIL_APIKEY_PUBLIC = '...'
YANDEX_MAIL_APIKEY_PRIVATE = '...'

GOOGLE_MAIL_SERVER = "smtp.gmail.com"
GOOGLE_MAIL_PORT = '587'
GOOGLE_MAIL_USE_TLS = 'False'
GOOGLE_MAIL_USE_SSL = 'True'
GOOGLE_MAIL_USERNAME = '...'
GOOGLE_MAIL_PASSWORD = '***'
GOOGLE_MAIL_APIKEY_PUBLIC = '...'
GOOGLE_MAIL_APIKEY_PRIVATE = '...'

if MAIL_SERVER_PROVIDER == 'GREENJET':
    MAIL_SERVER = GREENJET_MAIL_SERVER
    MAIL_PORT = GREENJET_MAIL_PORT
    MAIL_USE_TLS = GREENJET_MAIL_USE_TLS
    MAIL_USE_SSL = GREENJET_MAIL_USE_SSL
    MAIL_USERNAME = GREENJET_MAIL_USERNAME
    MAIL_PASSWORD = GREENJET_MAIL_PASSWORD
    MAIL_APIKEY_PUBLIC = GREENJET_MAIL_APIKEY_PUBLIC
    MAIL_APIKEY_PRIVATE = GREENJET_MAIL_APIKEY_PRIVATE
else:
    if MAIL_SERVER_PROVIDER == 'YANDEX':
        MAIL_SERVER = YANDEX_MAIL_SERVER
        MAIL_PORT = YANDEX_MAIL_PORT
        MAIL_USE_TLS = YANDEX_MAIL_USE_TLS
        MAIL_USE_SSL = YANDEX_MAIL_USE_SSL
        MAIL_USERNAME = YANDEX_MAIL_USERNAME
        MAIL_PASSWORD = YANDEX_MAIL_PASSWORD
        MAIL_APIKEY_PUBLIC = YANDEX_MAIL_APIKEY_PUBLIC
        MAIL_APIKEY_PRIVATE = YANDEX_MAIL_APIKEY_PRIVATE
    else:
        MAIL_SERVER = GOOGLE_MAIL_SERVER
        MAIL_PORT = GOOGLE_MAIL_PORT
        MAIL_USE_TLS = GOOGLE_MAIL_USE_TLS
        MAIL_USE_SSL = GOOGLE_MAIL_USE_SSL
        MAIL_USERNAME = GOOGLE_MAIL_USERNAME
        MAIL_PASSWORD = GOOGLE_MAIL_PASSWORD
        MAIL_APIKEY_PUBLIC = GOOGLE_MAIL_APIKEY_PUBLIC
        MAIL_APIKEY_PRIVATE = GOOGLE_MAIL_APIKEY_PRIVATE

################################################################
log_config_param('MAIL_SERVER', MAIL_SERVER)
log_config_param('MAIL_PORT', MAIL_PORT)
log_config_param('MAIL_USE_TLS', MAIL_USE_TLS)
log_config_param('MAIL_USE_SSL', MAIL_USE_SSL)
log_config_param('MAIL_USERNAME', MAIL_USERNAME)
log_config_param('MAIL_PASSWORD', MAIL_PASSWORD)
log_config_param('MAIL_APIKEY_PUBLIC', MAIL_APIKEY_PUBLIC)
log_config_param('MAIL_APIKEY_PRIVATE', MAIL_APIKEY_PRIVATE)
################################################################

log_config_finish(__file__, 'mailserver_configuration')
