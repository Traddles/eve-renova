from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, exc
from sqlalchemy.orm import mapper, relationship, backref
from database import metadata, db_session, Base, DB_PATH, init_db
import datetime

class Unit(Base):
    __tablename__ = 'units'
    #query = db_session.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    state = Column(Integer, nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_updated = Column(DateTime, onupdate=datetime.datetime.now)

    responsible = Column(String(50))

    allowed_states = {'state': {0: 'heating on', 1: '8-degrees'}}
    #print "AC HEATING"
        
    def __init__(self, name=None, state=None):
        self.name = name
        self.state = state
        # if('ac_heating' in self.name):
        #     print "AC HEATING"
        # else:
        #     self.allowed_states = {'state': {0: 'on', 1: 'off'}}
        #     print "ON OFF"

    def __repr__(self):
        return '<Unit %r: %r>' % (self.name, self.state)

    @staticmethod
    def objects(id = -1):
        if id is -1:
            entries =  []
            try:
                entries = Unit.query.all()
            except exc.SQLAlchemyError:
                pass
            return entries
        else:
            return Unit.query.get(id)

    def save(self):
        db_session.add(self)
        db_session.commit()

# units = Table(Unit.table_name, metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(30), unique=True, nullable=False),
#     Column('state', String(30), nullable=False),
#     Column('create_date', DateTime, default=datetime.datetime.now),
#     Column('last_updated', DateTime, onupdate=datetime.datetime.now),

#     Column('responsible', String(50))
#     #Column("unit_type"),

# )
# mapper(Unit, units)



# class AllowedStates(Base):
#     __tablename__ = 'units_allowed_states'

#     id = Column(Integer, primary_key = True)
#     name = Column(String(30))


# class UnitState(Base):
#     __tablename__ = 'unit_state'

#     unit_id = Column(Integer, ForeignKey('units.id'), primary_key=True)
#     allowed_state_id = Column(Integer, ForeignKey('units_allowed_states.id'), primary_key=True)
#     role_name = Column(String(30))

#     state = relationship("AllowedStates", backref="state_units")
#     unit = relationship("Unit", backref="unit_states")

