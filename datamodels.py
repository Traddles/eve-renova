from flask.ext.mongoengine import MongoEngine
import datetime

# engine = MongoEngine()
# engine.connect(db='eve')

from models import Unit, db_session

# Model
# class Unit(engine.DynamicDocument):
# 	created_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_created")
# 	updated_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_updated")
# 	allowed_fields = engine.DictField(required=False, db_field ="_allowed_fields")
# 	field_types = engine.DictField(required=False, db_field ="_field_types")
# 	name = engine.StringField(max_length=30, required=True)
# 	state = engine.StringField(max_length=30, required=False)
# 	def __unicode__(self):
# 		return self.name

