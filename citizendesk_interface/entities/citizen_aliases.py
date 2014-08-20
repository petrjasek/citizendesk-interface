entity = {
    'schema': {
        'authority': {
            'type': 'string'
        },
        'name_full': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'time_zone': {
            'type': 'string'
        },
        'identifiers': {
            'type': 'dict',
            'schema': {
                'user_name_search': {
                    'type': 'string'
                },
                'user_name': {
                    'type': 'string'
                },
            },
        },
        'avatars': {
            'type': 'list',
            'schema': {
                'https': {
                    'type': 'string'
                },
            },
        },
        'tags': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'citizen_lists',
                    'field': '_id',
                    'embeddable': True
                }
            }
        }
    },
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PATCH'],
    'pagination': False,
}
