import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.user_event import Base

class PostgresConnector():
    def __init__(self, logger, environment):
        self.logger = logger
        self.env = environment
        
    def connect(self,user,pswd,host,port,db):
        self.__connection_string='postgresql+psycopg2://{user}:{pswd}@{host}:{port}/{db}'.format(
            user=user,
            pswd=pswd,
            host=host,
            port=port,
            db=db
        )
        self.__engine = sqlalchemy.create_engine(self.__connection_string, echo=False)
        self.__address = '{user}@{host}:{port}/{db}'.format(
            user=user,
            host=host,
            port=port,
            db=db
        )
    
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

    def create_tables(self):
        Base.metadata.create_all(self.__engine)

    def execute_stmt(self, stmt):
        self.session.execute(stmt)
        self.session.commit()

    @property
    def get_address(self):
        return self.__address