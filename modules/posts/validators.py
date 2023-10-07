create_post_schema = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'content': {'type': 'string'},
    },
    'required': ['title', 'content'],
    'additionalProperties': False
}
