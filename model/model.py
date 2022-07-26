import datetime
import os
import random

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker


Base = sqlalchemy.ext.declarative.declarative_base()


class Temper(Base):
    __tablename__ = 'temper'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_at = sqlalchemy.Column(sqlalchemy.String)
    updated_at = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.String)


class Model(object):

    def get_temperature(self):
        # test function
        temp = random.uniform(10, 30)
        return f'{temp:.2f}'
    
    def get_exec_datetime(self):
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        return now
    
    def get_init_info(self):
        print('init_info')

    def init_db(self, path):
        self.engine = sqlalchemy.create_engine('sqlite:///' + path)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def temp_create_db(self):
        Base.metadata.create_all(self.engine)

    def insert_temper_db(self, created_at, updated_at, temp_value):
        temper = Temper(
            created_at=created_at,
            updated_at=updated_at,
            value=temp_value
        )
        self.session.add(temper)
        self.session.commit()

    def select_db(self):
        temper_records = self.session.query(Temper).order_by(Temper.id.desc()).limit(10)
        for temp in temper_records:
            print(
                    temp.id,
                    temp.created_at,
                    temp.updated_at,
                    temp.value
                 )


if __name__ == '__main__':
    model = Model()

    date = model.get_exec_datetime()
    temp = model.get_temperature()
    print(temp)
#    db_file = os.getcwd() + '/db/temp_test.db'
#
#    model.init_db(db_file)
#    model.temp_create_db()
#    model.insert_temper_db(date, date, 10.5)
#    model.select_db()
