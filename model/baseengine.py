from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 

class BaseEngine(object):
    def __init__(self):
        self.engine = create_engine('sqlite:////home/kurihara/work/python/temp_sys/db/temper.db' )
        


class BaseSession(BaseEngine):
    def __init__(self):
        super().__init__()
        Session = sessionmaker(bind=self.engine) 
        self.session = Session()


