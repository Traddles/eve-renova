from flask.ext.mongoengine import MongoEngine
import datetime

engine = MongoEngine()
engine.connect(db='eve')

# Model
class Unit(engine.DynamicDocument):
	created_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_created")
	updated_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_updated")
	allowed_fields = engine.DictField(required=False, db_field ="_allowed_fields")
	field_types = engine.DictField(required=False, db_field ="_field_types")
	name = engine.StringField(max_length=30, required=True)
	state = engine.StringField(max_length=30, required=False)
	def __unicode__(self):
		return self.name


'''
Wanted form of a unit json-object:
{
    "_id" : ObjectId("587795bce7027101bf682a52"),
    "_created" : ISODate("2017-01-12T15:30:52.910Z"),
    "_updated" : ISODate("2017-01-12T15:51:20.000Z"),
    "_allowed_fields" : {
        "state" : {
            "1" : "on",
            "0" : "off"
        }
    },
    "_field_types" : {},
    "name" : "luft",
    "state" : "on",
    "_etag" : "742b709fa8aa97e57cb727327b4dbef35028f818"
}
'''
