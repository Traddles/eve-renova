#import os
#print os.environ.get('PORT')

# Mongo DB
#MONGO_HOST = 'localhost'
#MONGO_PORT = 27017
#MONGO_DBNAME = 'eve'

# CORS
# TODO: Set exact domain address to be allowed CORS
X_DOMAINS = '*'
X_HEADERS = ['Content-Type', 'If-Match']
#X_EXPOSE_HEADERS
#X_MAX_AGE

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
PUBLIC_METHODS = ['GET', 'PATCH', 'POST', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 30,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'state': {
        'type': 'string',
        'allowed': ["on", "off"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'room': {'type': 'string'},
            'level': {
		        'type': 'string',
		        'allowed': ["roof", "middle", "floor"],
            }
        },
    },
    'installed': {
        'type': 'datetime',
    },
}

unit = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'unit',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}


# Domain structure : {
# 	unit : { location: dict }
# 	allowed_types : dict
# }
DOMAIN = {'unit': unit}

