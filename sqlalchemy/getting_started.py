from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, Unicode, String
class Store(Base):
    __tablename__ = 'stores'
            
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), nullable=False)
    phone = Column(String(20))

Base.metadata.create_all(engine)
