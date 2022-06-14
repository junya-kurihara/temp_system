import datetime
import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker


class BaseEngine(object):
    def __init__(self):
        self.engine = sqlalchemy.create_engine('sqlite:////home/kurihara/work/python/temp_sys/db/temper.db' )
        

class BaseSession(BaseEngine):
    def __init__(self):
        super().__init__()
        Session = sessionmaker(bind=self.engine) 
        self.session = Session()


Base = sqlalchemy.ext.declarative.declarative_base()


class Temper(Base):
    __tablename__ = 'temper'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)
    value = sqlalchemy.Column(sqlalchemy.String)


class Migration(object):
    def __init__(self):
        self.e = BaseEngine().engine

    def temp_create_db(self):
        Base.metadata.create_all(self.e)


class Crud(BaseSession):
    def __init__(self):
        super().__init__()

    def write_db(self, created_at, updated_at, temp_value):
    
        temper = Temper(
                created_at = created_at,
                updated_at = updated_at,
                value = temp_value
                )
        self.session.add(temper)
        self.session.commit()

    def select_db(self):
        temper_records = self.session.query(Temper).all()
        for temp in temper_records:
            print(
                    temp.id, 
                    temp.created_at, 
                    temp.updated_at, 
                    temp.value
                 )
    

if __name__ == '__main__':
    cli = Crud()
    cli.select_db() 
