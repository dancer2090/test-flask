email = {
    'type': 'string',
    'pattern': '^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$',
    'minLength': 3,
    'description': 'Please, provide a valid email'
}
password = {'type': 'string',  'minLength': 8, 'description': 'Please, provide a valid password'}

register_user_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'email': email,
        'password': password,
    },
    'required': ['username', 'email', 'password'],
    'additionalProperties': False
}

user_authentication_schema = {
    'type': 'object',
    'properties': {
        'email': email,
        'password': password,
    },
    'required': ['email', 'password'],
    'additionalProperties': False
}


