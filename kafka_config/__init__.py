import os


# AUTHENTICATION
API_KEY = os.getenv('API_KEY', "OBK7AL57JANLSTYJ")
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', "https://psrc-kk5gg.europe-west3.gcp.confluent.cloud")
API_SECRET_KEY = os.getenv('API_SECRET_KEY', "oVu6PhV4kJDhHgEsCw6z7z/Gdhzk8wnyCYmC2+OJyCRSanKbOPl8+m//o5HTddck")
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', "pkc-lzoyy.europe-west6.gcp.confluent.cloud:9092")
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL', "SASL_SSL")
SSL_MECHANISM = os.getenv('SSL_MECHANISM', "PLAIN")
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY', 'PG4TJGIR7ZVIA5ET')
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', '2Xns46ev80VDO4I/DY3NMvGfItsrvNkkmEI57yFu9syMCH8Zzbi+GivsQaY2bL92')

# CONTENT
TOPIC = os.getenv('TOPIC', 'tweets')


def sasl_conf():
    conf = {
        'sasl.mechanism': SSL_MECHANISM,
        'bootstrap.servers': BOOTSTRAP_SERVER,
        'security.protocol': SECURITY_PROTOCOL,
        'sasl.username': API_KEY,
        'sasl.password': API_SECRET_KEY
                 }
    return conf


def schema_config():
    return {
        'url': ENDPOINT_SCHEMA_URL,
        'basic.auth.user.info': f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
    }


if __name__ == '__main__':
    sasl_conf()

