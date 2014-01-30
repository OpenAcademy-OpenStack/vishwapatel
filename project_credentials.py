def get_keystone_credentials():
    keystone_credentials = {}
    keystone_credentials['username'] = 'admin'
    keystone_credentials['password'] = 'password'
    keystone_credentials['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    keystone_credentials['tenant_name'] = 'demo'
    return keystone_credentials


def get_nova_credentials():
    nova_credentials = {}
    nova_credentials['username'] = 'admin'
    nova_credentials['api_key'] = 'password'
    nova_credentials['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    nova_credentials['project_id'] = 'demo'
    return nova_credentials
