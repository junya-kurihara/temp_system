import datetime
import random

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


engine = sqlalchemy.create_engine('sqlite:///db/test_sqlite.db')

Base = sqlalchemy.ext.declarative.declarative_base()


class Temper(Base):
    __tablename__ = 'temper'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)
    value = sqlalchemy.Column(sqlalchemy.Float)

def get_temper():
    temp_value = random.uniform(10, 30)
    return temp_value

def write_db(temp_value: float):

    Base.metadata.create_all(engine)
    
    Session = sqlalchemy.orm.sessionmaker(bind=engine) 
    session = Session()

    temper = Temper(
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            value=temp_value
            )
    session.add(temper)
    session.commit()

def select_db():

    Base.metadata.create_all(engine)
    
    Session = sqlalchemy.orm.sessionmaker(bind=engine) 
    session = Session()

    temper_records = session.query(Temper).all()
    for temp in temper_records:
        print(
                temp.id, 
                temp.created_at, 
                temp.updated_at, 
                temp.value
             )


if __name__ == '__main__':

    temp_value = get_temper()

    write_db(temp_value)

    select_db()
    
