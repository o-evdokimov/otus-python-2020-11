from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

metadata = MetaData()
#engine = create_engine('sqlite:///movies.sqlite', echo=True)
engine = create_engine('postgres://postgres:qwerty@localhost:5432/movies', echo=False)
Base = declarative_base(bind=engine)

session_maker = sessionmaker(bind=engine)
Session = scoped_session(session_maker)

