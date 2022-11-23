from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True,  index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    books = relationship('Book', back_populates='reader')
    

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    cover = Column(String, index=True)
    reader_id = Column(Integer, ForeignKey('users.id'))
    summary = Column(String, index=True)
    
    reader = relationship('User', back_populates='books')
    