entity = {
    'schema': {
        'name': {
            'type': 'string',
        },
        'type': {
            'type': 'string',
            'allowed': ['mobile', 'twitter']
        },
        'citizens': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'citizen_aliases',
                    'field': '_id',
                    'embeddable': True
                }
            }
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'DELETE', 'PATCH'],
    'pagination': False,
}
