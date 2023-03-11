import os


# AUTHENTICATION  - Fill the info in below
API_KEY = os.getenv('API_KEY', "")
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', "")
API_SECRET_KEY = os.getenv('API_SECRET_KEY', "")
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', "")
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL', "")
SSL_MECHANISM = os.getenv('SSL_MECHANISM', "")
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY', '')
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', '')

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

