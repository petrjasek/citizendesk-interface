entity = {
    'schema': {
        'name': {
            'type': 'string',
        },
        'variation': {
            'type': 'string',
            'allowed': [
                'label-default',
                'label-primary',
                'label-success',
                'label-info',
                'label-warning',
                'label-danger',
            ]
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
