from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper
from database import metadata, db_session
import datetime, dataset

class Unit(object):
    table_name = 'units'
    query = db_session.query_property()
    #id = Column(Integer, primary_key=True)


	#created_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_created")
	#updated_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_updated")
	#allowed_fields = Column("_allowed_fields")
	#field_types = Column("_field_types")
    #name = Column(String(30), unique=True, nullable=False)
	#state = Column(String(30), nullable=False)


    def __init__(self, name=None, state=None):
        self.name = name
        self.state = state

    def __repr__(self):
        return '<Unit %r>' % (self.name)

    @staticmethod
    def objects(id = -1):
        if id is -1:
            return Unit.query.all()
        else:
            return Unit.query.get(id)

    def save(self):
        db_session.add(self)
        db_session.commit()

units = Table(Unit.table_name, metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), unique=True, nullable=False),
    Column('state', String(30), nullable=False),
    Column('create_date', DateTime, default=datetime.datetime.now),
    Column('last_updated', DateTime, onupdate=datetime.datetime.now),

    Column('responsible', String(50))
    #Column("unit_type"),

    #Column("_allowed_fields"),

)
mapper(Unit, units)
