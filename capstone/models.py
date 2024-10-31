from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Director(Base):
    __tablename__ = 'Director'
    DirectorID = Column(Integer, primary_key=True)
    DirectorName = Column(String(255))

class Genre(Base):
    __tablename__ = 'Genre'
    GenreID = Column(Integer, primary_key=True)
    Genre = Column(String(50))

class Movie(Base):
    __tablename__ = 'Movie'
    MovieID = Column(Integer, primary_key=True)
    Title = Column(String(255), nullable=False)
    Year = Column(Integer)
    Certificate = Column(String(10))
    Duration = Column(Integer)
    Rating = Column(Float)
    Metascore = Column(Integer)
    DirectorID = Column(Integer, ForeignKey('Director.DirectorID'))
    GenreID = Column(Integer, ForeignKey('Genre.GenreID'))
    Description = Column(Text)
    ImageUrl = Column(String(225))
    
    director = relationship('Director')
    genre = relationship('Genre')
    tracker_entries = relationship('MovieTracker', back_populates='movie')

class Cast(Base):
    __tablename__ = 'Cast'
    CastID = Column(Integer, primary_key=True)
    MovieID = Column(Integer, ForeignKey('Movie.MovieID'))
    CastMember = Column(String(255))

    movie = relationship('Movie')

class User(Base):
    __tablename__ = 'users'
    UserID = Column(Integer, primary_key=True)
    Username = Column(String(50), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)

    movies = relationship('MovieTracker', back_populates='user')

class MovieTracker(Base):
    __tablename__ = 'movie_tracker'
    TrackerID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('users.UserID'))
    MovieID = Column(Integer, ForeignKey('Movie.MovieID'))
    Status = Column(String(50))
    
    user = relationship('User', back_populates='movies')
    movie = relationship('Movie', back_populates='tracker_entries')
