entity = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True
        },
        'description': {
            'type': 'string',
            'required': True
        },
    },
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PATCH'],
    'pagination': False,
}
