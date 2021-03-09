from .base import Base
from .movie import Movie
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    movie_id = Column(String, ForeignKey(Movie.imdbID), nullable=False)
    author = Column(String(32), nullable=False, default='', server_default='')
    title = Column(String(255), nullable=False, default='', server_default='')
    text = Column(String(255), nullable=False, default='', server_default='')
    movie : Movie = relationship(Movie, back_populates='posts')
    created_at = Column(String)

    def __repr__(self):
        return f'\tPost: {self.title!r}\n\tAuthor: {self.author}\n\t\t{self.text!r}\n'


