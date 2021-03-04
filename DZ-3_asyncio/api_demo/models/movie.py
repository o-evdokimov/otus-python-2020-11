from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, collections

class Movie(Base):
    __tablename__ = 'movies'

    imdbID = Column(String, primary_key = True)
    Title = Column(String)
    Year = Column(String)
    Type =  Column(String)
    Poster = Column(String)
    created_at = Column(String)
    posts : collections.InstrumentedList = relationship("Post", back_populates='movie')

    def __repr__(self):
        return f'\tIMDB: {self.imdbID}\n\tTitle={self.Title!r}\n\tYear={self.Year}\n\tType={self.Type}\n'

